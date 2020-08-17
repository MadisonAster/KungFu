module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  //version = "2.44.0" //last tested version

  name                 = var.vpc_name
  cidr                 = var.vpc_cidr
  azs                  = var.vpc_azs
  private_subnets      = var.vpc_private_subnets
  public_subnets       = var.vpc_public_subnets
  //private_subnets      = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  //public_subnets       = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"] 
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