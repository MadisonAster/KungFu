variable "cluster_name" {
    description = "Name of EKS Cluster"
    type        = string
    default     = "KungFu_Cluster"
}
variable "kubenode_instance_type" {
    type        = string
    //default     = "t3.small"
    default     = "t3a.micro"
}
variable "region" {
    description = "Name of Aws Region"
    type        = string
    default     = "us-west-2"
}




variable "vpc_name" {
    description = "Name of VPC"
    type        = string
    default     = "KungFu_VPC"
}
variable "vpc_cidr" {
    description = "CIDR block for VPC"
    type        = string
    default     = "192.168.0.0/16"
}
variable "vpc_azs" {
    description = "Availability zones for VPC"
    type        = list
    default     = ["us-west-2a", "us-west-2b", "us-west-2c", "us-west-2d"]
}
variable "vpc_enable_nat_gateway" {
    description = "Enable NAT gateway for VPC"
    type        = bool
    default     = true
}
variable "enable_dns_support" {
    description = ""
    type        = bool
    default     = true
}
variable "enable_dns_hostnames" {
    description = ""
    type        = bool
    default     = true
}
variable "single_nat_gateway" {
    description = ""
    type        = bool
    default     = true
}
variable "vpc_private_subnets" {
    description = "Private subnets for VPC"
    type        = list(string)
    default     = ["192.168.0.0/18", "192.168.64.0/18"]
}
variable "vpc_public_subnets" {
    description = "Public subnets for VPC"
    type        = list(string)
    default     = ["192.168.128.0/18", "192.168.192.0/18"]
}




variable "public_key_path" {
    description = "Key Path"
    type        = string
    default     = "/usr/local/keys/MasterKey1.pub"
}
variable "private_key_path" {
    description = "Key Path"
    type        = string
    default     = "/usr/local/keys/MasterKey1.pem"
}




variable "map_accounts" {
    description = "Additional AWS account numbers to add to the aws-auth configmap."
    type        = list(string)
    default = [
        "777777777777",
        "888888888888",
    ]
}
variable "map_roles" {
    description = "Additional IAM roles to add to the aws-auth configmap."
    type = list(object({
        rolearn  = string
        username = string
        groups   = list(string)
    }))

    default = [
        {
            rolearn  = "arn:aws:iam::66666666666:role/role1"
            username = "role1"
            groups   = ["system:masters"]
        },
    ]
}
variable "map_users" {
    description = "Additional IAM users to add to the aws-auth configmap."
    type = list(object({
        userarn  = string
        username = string
        groups   = list(string)
    }))

    default = [
        {
            userarn  = "arn:aws:iam::66666666666:user/user1"
            username = "user1"
            groups   = ["system:masters"]
        },
        {
            userarn  = "arn:aws:iam::66666666666:user/user2"
            username = "user2"
            groups   = ["system:masters"]
        },
    ]
}
