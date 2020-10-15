output "vpc_id" {
    value = module.EKSCluster.vpc_id
}
output "vpc_name" {
    value = var.vpc_name
}

output "default_securitygroup" {
    value = module.EKSCluster.default_security_group_id
}

output "private_key_path" {
    value = var.private_key_path
}

output "cluster_id" {
    value = module.EKSCluster.cluster_id
}

output "cluster_name" {
    value = var.cluster_name
}

output "cluster_security_group_id" {
    description = "Security group ids attached to the cluster control plane."
    value       = module.EKSCluster.cluster_security_group_id
}

output "kubectl_config" {
    description = "kubectl config as generated by the module."
    value       = module.EKSCluster.kubeconfig
}

output "config_map_aws_auth" {
    description = "A kubernetes configuration to authenticate to this EKS cluster."
    value       = module.EKSCluster.config_map_aws_auth
}