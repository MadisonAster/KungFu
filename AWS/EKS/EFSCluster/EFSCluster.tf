terraform {
  required_version = ">= 0.12.0"
}

module "EKSCluster" {
  source = "../EKSCluster"
}


resource "aws_efs_file_system" "KungFu_FileSystem" {
  creation_token = var.efs_name
  performance_mode = "generalPurpose"
  throughput_mode = "bursting"
  encrypted = "true"
  tags = {
    Name = var.efs_name
    Terraform = "true"
    Environment = "test"
  }
}

resource "aws_efs_mount_target" "KungFu_MountTargets" {
  count = length(module.vpc.public_subnets)

  file_system_id  = aws_efs_file_system.KungFu_FileSystem.id
  subnet_id = element(module.vpc.public_subnets, count.index)
  security_groups = [
    module.vpc.default_security_group_id,
    aws_security_group.KungFu_ControlPlaneSecurityGroup.id,
    aws_security_group.KungFu_WebserverSecurityGroup.id,
    aws_security_group.KungFu_DataScraperSecurityGroup.id,
  ]
}




