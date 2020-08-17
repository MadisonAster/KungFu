
resource "aws_efs_mount_target" "${var.aws_efs_mount_target_name}" {
  count = length(module.vpc.public_subnets)

  file_system_id  = aws_efs_file_system.ResumePPFileSystem.id
  subnet_id = element(module.vpc.public_subnets, count.index)
  security_groups = [
    module.vpc.default_security_group_id,
    aws_security_group.ControlPlaneSecurityGroup.id,
    aws_security_group.WebserverSecurityGroup.id,
    aws_security_group.DataScraperSecurityGroup.id,
  ]
}


