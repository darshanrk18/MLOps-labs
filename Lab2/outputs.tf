output "ec2_instance_id" {
  value       = aws_instance.lab_ec2.id
  description = "EC2 instance ID"
}

output "ec2_public_ip" {
  value       = aws_instance.lab_ec2.public_ip
  description = "EC2 public IP address"
}
