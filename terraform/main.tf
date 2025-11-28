terraform {
required_version = ">= 1.2"
}


provider "aws" {
region = var.aws_region
}


resource "aws_s3_bucket" "mlflow_bucket" {
bucket = "${var.project_prefix}-mlflow-bucket-${random_id.bucket.hex}"
acl = "private"
force_destroy = true
}


resource "random_id" "bucket" { byte_length = 4 }


# RDS Postgres for app + mlflow backend
module "db" {
source = "terraform-aws-modules/rds/aws"
engine = "postgres"
engine_version = "13.9"
instance_type = "db.t3.micro"
allocated_storage = 20
name = "medlab"
username = var.db_user
password = var.db_password
publicly_accessible = false
}


# EKS cluster (minimal)
module "eks" {
source = "terraform-aws-modules/eks/aws"
cluster_name = "${var.project_prefix}-eks"
cluster_version = "1.26"
subnets = var.private_subnets
vpc_id = var.vpc_id
node_groups = {
default = {
desired_capacity = 2
instance_type = "t3.medium"
}
}
}
