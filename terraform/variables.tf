variable "aws_region" { default = "us-east-1" }
variable "project_prefix" { default = "medlab" }
variable "db_user" { type = string }
variable "db_password" { type = string }
variable "vpc_id" { type = string }
variable "private_subnets" { type = list(string) }
