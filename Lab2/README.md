# Lab 2: Terraform Beginner Lab

Deploy AWS infrastructure (VPC, subnet, EC2) using Terraform. This lab demonstrates Infrastructure as Code (IaC) fundamentals.

---

## Objective

- Understand Terraform and its purpose
- Write and apply a Terraform configuration
- Use Terraform commands to create, modify, and destroy infrastructure
- Use variables and outputs for maintainable configurations

---

## What This Lab Creates

| Resource | Description |
|----------|-------------|
| **VPC** | Virtual private cloud (10.10.0.0/16) with DNS support |
| **Public Subnet** | Subnet (10.10.1.0/24) with auto-assign public IP |
| **Internet Gateway** | Enables internet access for the subnet |
| **Route Table** | Routes traffic to the IGW |
| **Security Group** | SSH (port 22) allowed only from your IP |
| **EC2 Instance** | t2.micro in the public subnet |

---

## Prerequisites

- [AWS account](https://aws.amazon.com/)
- [Terraform installed](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) (>= 1.5.0)
- AWS access keys configured

### Create AWS Access Keys

1. Open AWS Console → IAM → Security credentials
2. Click **Create access key**
3. Copy **Access key ID** and **Secret access key** (secret is shown only once)
4. Store them securely

### Set Environment Variables

```bash
export AWS_ACCESS_KEY_ID=<your-access-key-id>
export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
```

---

## Project Structure

```
Lab2/
├── main.tf              # VPC, subnet, EC2, security group
├── variables.tf         # Input variables
├── outputs.tf           # Output values
├── terraform.tfvars     # Your variable values (create from example)
└── terraform.tfvars.example
```

---

## Steps to Re-run This Lab

### 1. Clone and navigate

```bash
git clone <your-repo-url>
cd MLOps-labs/Lab2
```

### 2. Configure variables

Copy the example file and set your values:

```bash
cp terraform.tfvars.example terraform.tfvars
```

Edit `terraform.tfvars` and set `my_ip_cidr` to your public IP in CIDR format (e.g., `1.2.3.4/32`). Find your IP at [whatismyip.com](https://www.whatismyip.com/).

### 3. Initialize Terraform

```bash
terraform init
```

### 4. Review the plan

```bash
terraform plan
```

### 5. Apply the configuration

```bash
terraform apply
```

Type `yes` when prompted, or use `terraform apply -auto-approve` to skip confirmation.

### 6. View outputs

```bash
terraform output
```

### 7. Destroy resources when done

```bash
terraform destroy
```

Type `yes` to confirm.

---

## Terraform Commands Reference

| Command | Purpose |
|---------|---------|
| `terraform init` | Initialize providers and backend |
| `terraform plan` | Preview changes |
| `terraform apply` | Create or update infrastructure |
| `terraform destroy` | Remove all managed resources |
| `terraform output` | Show output values |

---

## Variables (Optional Overrides)

All variables have defaults in `variables.tf`. Override in `terraform.tfvars` or via `-var`:

| Variable | Default | Description |
|----------|---------|-------------|
| `project_name` | darshan-tf-lab | Prefix for resource names |
| `aws_region` | us-east-1 | AWS region |
| `az` | us-east-1a | Availability zone |
| `instance_type` | t2.micro | EC2 instance type |
| `ami_id` | ami-0e2c8caa4b6378d8c | AMI for us-east-1 |
| `my_ip_cidr` | (required) | Your IP in CIDR format, e.g. 1.2.3.4/32 |

---

## Notes

- **State file** (`terraform.tfstate`) is created after `apply` and tracks managed resources. Do not edit it manually.
- **terraform.tfvars** is gitignored to avoid committing your IP or secrets.
- Ensure `my_ip_cidr` matches your current public IP; update it if your IP changes.
