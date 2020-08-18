variable "cluster_name" {
  description = "Name of EKS Cluster"
  type        = string
  default     = "KungFuCluster"
}

variable "vpc_name" {
  description = "Name of VPC"
  type        = string
  default     = "KungFuVPC"
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
  type    = bool
  default = true
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

variable "enable_dns_support" {
  description = ""
  type    = bool
  default = true
}

variable "enable_dns_hostnames" {
  description = ""
  type    = bool
  default = true
}

variable "single_nat_gateway" {
  description = ""
  type    = bool
  default = true
}
