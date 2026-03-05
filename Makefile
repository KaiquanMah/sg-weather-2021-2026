# Load environment variables from .env file if it exists
ifneq ($(wildcard .env),)
    include .env
    # Remove quotes from variables
    PROJECT_ID := $(strip $(PROJECT_ID))
    PROJECT_ID := $(subst ",,$(PROJECT_ID))
    REGION := $(strip $(REGION))
    REGION := $(subst ",,$(REGION))
endif

.PHONY: help install test lint terraform-init terraform-plan terraform-apply terraform-destroy run-ingestion

# Display help message
help:
	@echo "Usage:"
	@echo "  make install              Install dependencies"
	@echo "  make test                 Run unit tests"
	@echo "  make lint                 Lint code with flake8"
	@echo "  make terraform-init       Initialize Terraform"
	@echo "  make terraform-plan       Plan Terraform changes"
	@echo "  make terraform-apply      Apply Terraform changes"
	@echo "  make terraform-destroy    Destroy Terraform resources"
	@echo "  make run-ingestion        Run the weather data ingestion pipeline"

# Install dependencies
install:
	pip install -r requirements.txt

# Run unit tests
test:
	python -m pytest tests/ -v

# Lint code
lint:
	flake8 scripts/ --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 scripts/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Terraform commands
terraform-init:
	cd terraform && terraform init

terraform-plan:
	@if [ -z "$(PROJECT_ID)" ]; then \
		echo "Error: PROJECT_ID is not set. Usage: make terraform-plan PROJECT_ID=your-project-id"; \
		exit 1; \
	fi
	cd terraform && terraform plan \
		-var="project_id=$(PROJECT_ID)" \
		-var="region=$(REGION)"

terraform-apply:
	@if [ -z "$(PROJECT_ID)" ]; then \
		echo "Error: PROJECT_ID is not set. Usage: make terraform-apply PROJECT_ID=your-project-id"; \
		exit 1; \
	fi
	cd terraform && terraform apply \
		-var="project_id=$(PROJECT_ID)" \
		-var="region=$(REGION)" \
		-auto-approve

terraform-destroy:
	@if [ -z "$(PROJECT_ID)" ]; then \
		echo "Error: PROJECT_ID is not set. Usage: make terraform-destroy PROJECT_ID=your-project-id"; \
		exit 1; \
	fi
	cd terraform && terraform destroy \
		-var="project_id=$(PROJECT_ID)" \
		-var="region=$(REGION)" \
		-auto-approve

# Run ingestion pipeline
run-ingestion:
	python scripts/ingest.py

# Run single date ingestion
run-single-date:
	python -c "from scripts.ingest import run_single_date; run_single_date('$(DATE)')"