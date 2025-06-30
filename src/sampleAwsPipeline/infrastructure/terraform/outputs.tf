output "eks_cluster_name" {
  value = module.eks.cluster_name
}
output "kubeconfig_path" {
  value = var.kubeconfig
}