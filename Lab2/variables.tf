variable "project_name" {
  type        = string
  description = "Prefix for naming AWS resources"
  default     = "darshan-tf-lab"
}

variable "aws_region" {
  type        = string
  description = "AWS region to deploy resources into"
  default     = "us-east-1"
}

variable "az" {
  type        = string
  description = "Availability Zone for subnet"
  default     = "us-east-1a"
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "ami_id" {
  type        = string
  description = "AMI ID for EC2 (region-specific)"
  # Keep your original AMI if you want; changing it is also fine.
  default = "ami-0e2c8caa4b6378d8c"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR block for VPC"
  default     = "10.10.0.0/16"
}

variable "public_subnet_cidr" {
  type        = string
  description = "CIDR block for public subnet"
  default     = "10.10.1.0/24"
}

variable "my_ip_cidr" {
  type        = string
  description = "Your public IP in CIDR format (example: 1.2.3.4/32)"
}
