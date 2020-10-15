output "efs_id" {
    value = aws_efs_file_system.KungFu_FileSystem.id
}
output "efs_name" {
    value = var.efs_name
}

output "mount_targets" {
    value = aws_efs_mount_target.KungFu_MountTargets
}


output "EKSCluster" {
    value = module.EKSCluster
}