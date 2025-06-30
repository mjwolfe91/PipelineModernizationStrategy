module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = var.cluster_name
  cluster_version = "1.28"
  vpc_id          = var.vpc_id
  enable_irsa     = true
  tags = {
    Environment = "dev"
  }
}

provider "helm" {
  kubernetes {
    config_path = var.kubeconfig
  }
}

resource "helm_release" "spark_pipeline" {
  name       = "spark-pipeline"
  chart      = "../spark-pipeline"
  namespace  = "data-pipeline"
  create_namespace = true
  values     = [file("../my-values.yaml")]
  depends_on = [module.eks]
}
