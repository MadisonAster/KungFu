output "ebs_id" {
    value = aws_ebs_file_system.KungFu_FileSystem.id
}
output "ebs_name" {
    value = var.ebs_name
}

output "mount_targets" {
    value = aws_ebs_mount_target.KungFu_MountTargets
}


output "EKSCluster" {
    value = module.EKSCluster
}