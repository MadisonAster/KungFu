resource "aws_efs_file_system" "${efs_name}" {
  creation_token = var.efs_name
  performance_mode = "generalPurpose"
  throughput_mode = "bursting"
  encrypted = "true"
  tags = {
    Name = var.efs_name
    Terraform = "true"
    Environment = "test"
  }
}