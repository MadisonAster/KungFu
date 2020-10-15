terraform {
    required_version = ">= 0.12.0"
}
provider "aws" {
    version = ">= 2.28.1"
    region  = var.region
}
provider "random" {
    version = "~> 2.1"
}
provider "local" {
    version = "~> 1.2"
}
provider "null" {
    version = "~> 2.1"
}
provider "template" {
    version = "~> 2.1"
}

data "aws_eks_cluster" "cluster" {
    name = module.eks.cluster_id
}
data "aws_eks_cluster_auth" "cluster" {
    name = module.eks.cluster_id
}

provider "kubernetes" {
    host                   = data.aws_eks_cluster.cluster.endpoint
    cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
    token                  = data.aws_eks_cluster_auth.cluster.token
    load_config_file       = false
    //version                = "~> 1.17"
    version                = "~> 1.11" //I don't understand where this version number comes from
}

data "aws_availability_zones" "available" {
}

resource "random_string" "suffix" {
    length  = 8
    special = false
}

resource "aws_security_group" "ControlPlaneSecurityGroup" {
    name_prefix     = "ControlPlaneSG"
    vpc_id          = module.vpc.vpc_id

    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port   = 2049
        to_port     = 2049
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        from_port   = 2049
        to_port     = 2049
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port   = 443
        to_port     = 443
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_security_group" "KubeNodeSecurityGroup" {
    name_prefix     = "KubeNodeSG"
    vpc_id          = module.vpc.vpc_id
    ingress {
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

module "vpc" {
    source  = "terraform-aws-modules/vpc/aws"
    //version = "2.44.0" //last tested version

    name                 = var.vpc_name
    cidr                 = var.vpc_cidr
    azs                  = var.vpc_azs
    private_subnets      = var.vpc_private_subnets
    public_subnets       = var.vpc_public_subnets
    enable_nat_gateway   = var.vpc_enable_nat_gateway
    enable_dns_support   = var.enable_dns_support
    enable_dns_hostnames = var.enable_dns_hostnames
    single_nat_gateway   = var.single_nat_gateway
    
    tags = {
        "kubernetes.io/cluster/${var.cluster_name}"   = "shared"
    }
    public_subnet_tags = {
        "kubernetes.io/cluster/${var.cluster_name}"   = "shared"
        "kubernetes.io/role/elb"                      = "1"
    }
    private_subnet_tags = {
        "kubernetes.io/cluster/${var.cluster_name}"   = "shared"
        "kubernetes.io/role/internal-elb"             = "1"
    }
}


module "eks" {
    source       = "terraform-aws-modules/eks/aws"
    //version                            = "12.2.0" //last tested version
    cluster_version                      = "1.17"
    cluster_name                         = var.cluster_name
    vpc_id                               = module.vpc.vpc_id
    subnets                              = module.vpc.private_subnets
    cluster_security_group_id            = aws_security_group.ControlPlaneSecurityGroup.id
    //manage_aws_auth = false
    map_roles                            = var.map_roles
    map_users                            = var.map_users
    map_accounts                         = var.map_accounts
    tags = {
      Name = var.cluster_name
    }
    
    node_groups = {
        KubeNodeGroup = {
            instance_type                 = var.kubenode_instance_type
            //additional_userdata           = ""
            asg_desired_capacity          = 1
            asg_max_size                  = 1
            additional_security_group_ids = [
                module.vpc.default_security_group_id,
                aws_security_group.ControlPlaneSecurityGroup.id,
                aws_security_group.KubeNodeSecurityGroup.id
            ]
            ssh = {
                allow = true
                publicKeyPath = var.public_key_path
                sourceSecurityGroupIds = [
                    module.vpc.default_security_group_id,
                    aws_security_group.ControlPlaneSecurityGroup.id,
                    aws_security_group.KubeNodeSecurityGroup.id
                ]
            }
            labels = {
                app = "KubeNode"
            }
            tags = {
                app = "KubeNode"
            }
        }
    }
}