# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

locals {
  web_instance_type_map = {
    stage = "t3.micro"
    prod = "t3.large"
  }
  web_instance_count_map = {
    stage = 1
    prod = 2
  }
  instances = {
    "t3.micro" = "ami-00514a528eadbc95b"
    "t3.large" = "ami-00514a528eadbc95b"
  }
}

resource "aws_instance" "web2" {
  ami = "ami-00514a528eadbc95b"
  instance_type = "local.web_instance_type_map[terraform.workspace]"
  count = local.web_instance_count_map[terraform.workspace]
  tags = {
    Name = "HelloWorld"
  }
}

resource "aws_instance" "web" {
  for_each = local.instances

  ami = each.value
  instance_type = each.key
  tags = {
    Name = "HelloWorld"
  }
  lifecycle {
    create_before_destroy = true
  }
}

