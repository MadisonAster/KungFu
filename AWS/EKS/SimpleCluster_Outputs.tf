
//output "KungFu_FileSystem" {
//  value = aws_efs_file_system.KungFu_FileSystem.id
//}

//output "KungFu_FileSystemDNS" {
//  value = aws_efs_mount_target.KungFu_MountTargets[0].dns_name
//}

//output "KungFu_GitControlID" {
//  value = module.ec2_instances.KungFu_GitInstance.id
//}

//output "KungFu_GitControlDNS" {
//  value = module.ec2_instances.KungFu_GitInstance.dns
//}

//output "WebserverSecurityGroup" {
//  value = aws_security_group.WebserverSecurityGroup.id
//}

//output "DataScraperSecurityGroup" {
//  value = aws_security_group.DataScraperSecurityGroup.id
//}

output "vpc_id" {
  value = module.vpc.vpc_id
}

output "default_securitygroup" {
  value = module.vpc.default_security_group_id
}

output "aws_account_id" {
  value = var.aws_account_id
}

output "aws_user_id" {
  value = var.aws_user_id
}

output "aws_region" {
  value = var.aws_region
}

output "private_key_path" {
  value = var.private_key_path
}

output "cluster_id" {
  value       = module.eks.cluster_id
}

output "cluster_name" {
  value       = var.cluster_name
}
