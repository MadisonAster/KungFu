output "vpc_id" {
    value = module.vpc.vpc_id
}
output "vpc_name" {
    value = var.vpc_name
}
output "public_subnets" {
    value = module.vpc.public_subnets
}

output "default_security_group_id" {
    value = module.vpc.default_security_group_id
}
output "KubeNodeSecurityGroup" {
    value = aws_security_group.KubeNodeSecurityGroup
}
output "ControlPlaneSecurityGroup" {
    value = aws_security_group.ControlPlaneSecurityGroup
}
output "cluster_id" {
    value = module.eks.cluster_id
}
output "cluster_name" {
    value = var.cluster_name
}
output "cluster_endpoint" {
    description = "Endpoint for EKS control plane."
    value       = module.eks.cluster_endpoint
}
output "cluster_security_group_id" {
    description = "Security group ids attached to the cluster control plane."
    value       = module.eks.cluster_security_group_id
}

output "kubeconfig" {
    value = module.eks.kubeconfig
}
output "config_map_aws_auth" {
    description = "A kubernetes configuration to authenticate to this EKS cluster."
    value       = module.eks.config_map_aws_auth
}

output "fargate_profile_name" {
    value = var.fargate_profile_name
}
output "kubernetes_namespace" {
    value = var.kubernetes_namespace
}
