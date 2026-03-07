# Singapore Weather Analytics Pipeline (2021-2026)

Data Engineering Zoomcamp 2026 Project - Ingestion and Visualization of Historical Weather Data from data.gov.sg APIs

## Problem Statement

Singapore weather analysts need historical insights (Jan 2021–Feb 2026) 
across 4 metrics (temperature, humidity, rainfall, wind speed) from 15+ stations. 
Current data is siloed in real-time APIs with pagination limits, making trend 
analysis and dashboarding difficult.

Solution: Build a batch ingestion pipeline that:
1. Backfills historical data from APIs using date-range queries
2. Stores raw data in a data lake (GCS) + structured tables in BigQuery
3. Transforms data for analytics (unified schema, station metadata enrichment)
4. Powers a Looker Studio dashboard with temporal + categorical visualizations

## Architecture Diagram

```mermaid
graph LR
    A[Start: Date Range Config<br/>2021-01-01 to 2026-02-28] --> B[Python Ingestion Task]
    B --> C{For each API + date}
    C --> D[Call API with ?date=YYYY-MM-DD]
    D --> E[Handle paginationToken<br/>if response has next page]
    E --> F[Parse JSON → pandas DataFrame]
    F --> G[Add meta api_name, ingest_timestamp]
    G --> H[Write to GCS as Parquet<br/>gs://weather-raw/{api}/{date}.parquet]
    H --> I[Load to BigQuery raw table<br/>Partitioned by date]
    I --> J[Kestra orchestration: create unified view]
    J --> K[BigQuery analytics table<br/>Partitioned + Clustered]
    K --> L[Looker Studio Dashboard]
```

## Prerequisites

- GCP project with billing enabled
- data.gov.sg API key (sign up [here](https://data.gov.sg))
- Python 3.11
- Terraform v1.5+
- Git

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/sg-weather-2021-2026.git
cd sg-weather-2021-2026
```

### 2. Set Environment Variables

Create a `.env` file or export these variables:

```bash
export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
export DATA_GOV_SG_API_KEY="your-api-key"
export PROJECT_ID="your-gcp-project-id"
export REGION="asia-southeast1"  # or your preferred region
export BIGQUERY_DATASET_ID="weather_data"
export GCS_BUCKET_NAME="your-bucket-name"
```

### 3. Install Dependencies

```bash
make install
```

Or manually:
```bash
pip install -r requirements.txt
```

then install terraform - failed in GitHub Codespace
```bash
# Install prerequisites
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl

# Add the HashiCorp GPG key:
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

# Add the HashiCorp repository:
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

# Install Terraform:
sudo apt update && sudo apt install -y terraform

# verify terraform has been installed
terraform version
```

Install Terraform via Direct Binary Download
```bash
# Set the Terraform version you want (check latest: https://www.terraform.io/downloads.html)
TERRAFORM_VERSION="1.9.0"

# Download the zip file
curl -O "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip"

# Install unzip if not present
sudo apt-get install -y unzip

# Extract ONLY the terraform binary directly to /usr/local/bin
unzip -j "terraform_${TERRAFORM_VERSION}_linux_amd64.zip" terraform -d /tmp/
sudo mv /tmp/terraform /usr/local/bin/
sudo chmod +x /usr/local/bin/terraform

# Clean up
rm "terraform_${TERRAFORM_VERSION}_linux_amd64.zip"

# Verify
terraform version
# Terraform v1.9.0
# on linux_amd64
# Your version of Terraform is out of date! The latest version
# is 1.14.6. You can update by downloading from https://www.terraform.io/downloads.html
```


### 4. Provision Infrastructure

```bash
make terraform-init
make terraform-plan
make terraform-apply
```

### 5. Run the Ingestion Pipeline

For the full date range (Jan 2021 - Feb 2026):
```bash
make run-ingestion
```

For a single date:
```bash
make run-single-date DATE=2024-01-15
```

## Development Workflow

### Step-by-Step Guide

#### Step 1: Local Development Setup

1. **Clone and navigate to the project:**
   ```bash
   git clone https://github.com/yourname/sg-weather-2021-2026.git
   cd sg-weather-2021-2026
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   make install
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```bash
   GOOGLE_CLOUD_PROJECT=your-project-id
   DATA_GOV_SG_API_KEY=your-api-key
   PROJECT_ID=your-project-id
   REGION=asia-southeast1
   BIGQUERY_DATASET_ID=weather_data
   GCS_BUCKET_NAME=your-bucket-name
   ```

#### Step 2: Understanding the Code Structure

The project follows a modular architecture:

```
scripts/
├── config.py      # Configuration settings (API endpoints, GCP settings, rate limits)
├── api_client.py  # Handles API requests with retry logic and pagination
├── loaders.py     # Manages data loading to GCS and BigQuery
└── ingest.py      # Main orchestration script that ties everything together

tests/
├── test_api_client.py  # Unit tests for API client
└── test_loaders.py     # Unit tests for data loaders

terraform/
├── main.tf      # GCP infrastructure (BigQuery, GCS)
├── variables.tf # Input variables
└── outputs.tf   # Output values

kestra/
└── weather_pipeline.yaml  # Workflow orchestration definition

dbt/
├── dbt_project.yml       # dbt project configuration
├── sources.yml           # Source definitions
└── models/               # Transformation models
```

#### Step 3: Running Tests

Before making any changes, ensure all tests pass:

```bash
make test
```

This runs pytest on all test files. The tests use mocking to avoid actual API calls and GCP resource usage.

**Test coverage:**
- `test_api_client.py`: Tests API request handling, rate limiting, pagination, and error cases
- `test_loaders.py`: Tests GCS uploads, BigQuery loads, and data transformations

#### Step 4: Making Code Changes

1. **Create a new branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** in the appropriate module:
   - Modify `config.py` for configuration changes
   - Update `api_client.py` for API interaction logic
   - Change `loaders.py` for data loading transformations
   - Edit `ingest.py` for workflow orchestration

3. **Run tests after each change:**
   ```bash
   make test
   ```

4. **Lint your code:**
   ```bash
   make lint
   ```

#### Step 5: Testing Locally

1. **Test with a single date first:**
   ```bash
   python -c "from scripts.ingest import run_single_date; run_single_date('2024-01-15')"
   ```

2. **Check logs** for any errors or warnings

3. **Verify data in GCS and BigQuery:**
   ```bash
   # Check GCS bucket
   gsutil ls gs://your-bucket-name/raw/
   
   # Query BigQuery
   bq query --use_legacy_sql=false "SELECT COUNT(*) FROM \`your-project.weather_data.raw_air_temperature\`"
   ```

#### Step 6: Deploying Infrastructure

1. **Initialize Terraform:**
   ```bash
   make terraform-init
   ```

2. **Review the plan:**
   ```bash
   make terraform-plan
   ```

3. **Apply changes:**
   ```bash
   make terraform-apply
   ```

#### Step 7: Running the Full Pipeline

Once infrastructure is ready and tests pass:

```bash
make run-ingestion
```

This will process all dates from Jan 2021 to Feb 2026. Monitor the logs for progress.

#### Step 8: CI/CD Integration

The project uses GitHub Actions for continuous integration:

- **On push/PR:** Runs tests and linting on Python 3.11
- **Terraform validation:** Checks TF syntax and formatting

To trigger CI:
1. Commit your changes: `git commit -m "Description"`
2. Push to your branch: `git push origin feature/your-feature-name`
3. Create a pull request

#### Step 9: Orchestration with Kestra

For production workflows, use Kestra:

1. **Deploy Kestra** to your environment
2. **Update** `kestra/weather_pipeline.yaml` with your project details
3. **Import** the workflow into Kestra UI
4. **Schedule** or manually trigger the pipeline

### Common Development Tasks

#### Adding a New Weather Metric

1. Add the endpoint to `Config.API_ENDPOINTS` in `config.py`
2. Update the table mapping in `loaders.py`
3. Add transformation logic in `_transform_data()` method
4. Create corresponding tests in `test_loaders.py`
5. Update dbt models if needed

#### Modifying Rate Limits

Edit these values in `config.py`:
```python
REQUEST_DELAY = 1.5  # seconds between API requests
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds between retries
```

#### Debugging Issues

1. **Enable verbose logging:**
   Add `logging.basicConfig(level=logging.DEBUG)` in your script

2. **Test API connectivity:**
from datetime import datetime
from scripts.api_client import WeatherAPIClient
client = WeatherAPIClient()
data = client.fetch_data_for_date("air-temperature", datetime(2024, 1, 15))
print(f"Fetched {len(data)} records")

3. **Check GCP credentials:**
   ```bash
   gcloud auth application-default login
   ```

## Testing

Run unit tests:
```bash
make test
```

Lint code:
```bash
make lint
```

### Test Suite Explanation

The project includes a comprehensive test suite with two main test files:

#### `test_api_client.py`
This test file validates the functionality of the API client that interacts with data.gov.sg APIs:

- **`test_make_request_success`**: Verifies that the `_make_request` method correctly handles successful API responses (status code 200)
- **`test_make_request_429_retry`**: Tests the rate limiting functionality by simulating HTTP 429 (Too Many Requests) responses and verifying that the client retries appropriately
- **`test_make_request_404_empty_response`**: Ensures the client handles cases where no data is found (HTTP 404) by returning an empty readings array
- **`test_fetch_data_for_date_formatting`**: Confirms that dates are properly formatted when calling the API endpoints
- **`test_fetch_all_data_for_date_calls_all_endpoints`**: Validates that the `fetch_all_data_for_date` method calls all four required API endpoints (temperature, humidity, rainfall, wind speed)

These tests use mocking to simulate API responses without making actual network requests, ensuring tests run quickly and reliably.

#### `test_loaders.py`
This test file verifies the data loading functionality to GCS and BigQuery:

- **`test_save_to_gcs`**: Tests that data is properly converted to Parquet format and saved to the correct GCS location with proper naming conventions
- **`test_load_to_bigquery`**: Ensures data is correctly loaded to BigQuery tables with proper schema mapping
- **`test_transform_data_*` (4 methods)**: Each method tests the transformation logic for one of the four weather data types (temperature, humidity, rainfall, wind speed), verifying that data is mapped to the correct fields with appropriate units
- **`test_load_weather_data_calls_correct_tables`**: Validates that the main loading function processes all four weather data types and calls the appropriate loading methods

The tests use mocking for GCP services (BigQuery and Cloud Storage) to avoid requiring actual cloud resources during testing, making the tests fast and cost-effective.

### Why These Tests Are Important

1. **Reliability**: Tests ensure that API interactions and data transformations work correctly under various conditions
2. **Maintainability**: When modifying code, tests catch regressions early
3. **Confidence**: Automated tests provide confidence that the pipeline works as expected
4. **Documentation**: Tests serve as executable documentation of expected behavior
5. **Cost Efficiency**: Testing with mocks prevents unnecessary API calls and cloud resource usage during development

## Orchestration with Kestra

The pipeline is orchestrated using Kestra, which handles:
- Parallel ingestion of multiple dates
- Error handling and retries
- Monitoring and logging
- Scheduling capabilities

To run the pipeline in Kestra:
1. Deploy Kestra to your environment
2. Update the pipeline configuration with your GCP project details
3. Submit the workflow using the Kestra CLI or UI

The Kestra workflow (`kestra/weather_pipeline.yaml`) implements the complete data pipeline:
- Generates the date range for backfill (Jan 2021 to Feb 2026)
- Processes dates in parallel using EachParallel task
- For each date, fetches data from all four weather APIs
- Loads data to GCS and BigQuery
- Creates the unified view in BigQuery after all data is loaded

## API Dataset
* air-temperature: [API documentation](https://data.gov.sg/datasets/d_66b77726bbae1b33f218db60ff5861f0/view), [API](https://api-open.data.gov.sg/v2/real-time/api/air-temperature)
* relative-humidity: [API documentation](https://data.gov.sg/datasets/d_2d3b0c4da128a9a59efca806441e1429/view), [API](https://api-open.data.gov.sg/v2/real-time/api/relative-humidity)
* rainfall: [API documentation](https://data.gov.sg/datasets/d_6580738cdd7db79374ed3152159fbd69/view), [API](https://api-open.data.gov.sg/v2/real-time/api/rainfall)
* wind-speed: [API documentation](https://data.gov.sg/datasets/d_7677738484067741bf3b56ab5d69c7e9/view), [API](https://api-open.data.gov.sg/v2/real-time/api/wind-speed)



## Data Model

The solution creates several BigQuery tables:

- `raw_air_temperature`: Raw air temperature readings
- `raw_relative_humidity`: Raw humidity readings  
- `raw_rainfall`: Raw rainfall measurements
- `raw_wind_speed`: Raw wind speed measurements
- `unified_weather`: Combined view of all weather data types

All tables are partitioned by date and clustered by station_id for optimal query performance.

The data transformation follows this flow:
1. Raw data is stored in date-partitioned tables for each weather metric
2. The unified table combines all weather types into a single view with appropriate null values
3. The unified table is also partitioned by date and clustered by station_id and reading_type

The dbt models in `dbt/models/` implement the transformation logic:
- Staging models clean and normalize the raw data
- The unified model combines all weather metrics into a single analytics table
- Schema definitions ensure data quality and consistency

## Dashboard

The Looker Studio dashboard includes:
- Temporal distribution: How weather metrics changed over time
- Categorical distribution: Comparison of metrics across different weather stations

The dashboard connects to the unified BigQuery table which contains all weather data types in a single view, making it easy to create visualizations that compare different weather metrics.

Sample queries for dashboard creation:
```sql
-- For temporal visualization (monthly averages)
SELECT 
  DATE_TRUNC(reading_timestamp, MONTH) AS month,
  AVG(temperature) AS avg_temperature,
  AVG(humidity) AS avg_humidity,
  AVG(rainfall) AS avg_rainfall,
  AVG(wind_speed) AS avg_wind_speed
FROM `your-project.weather_data.unified_weather`
GROUP BY month
ORDER BY month

-- For categorical visualization (by station)
SELECT 
  station_id,
  COUNT(*) AS reading_count,
  AVG(temperature) AS avg_temperature,
  AVG(humidity) AS avg_humidity
FROM `your-project.weather_data.unified_weather`
WHERE reading_type = 'temperature'
GROUP BY station_id
ORDER BY reading_count DESC
```

## Cost Estimate

- BigQuery storage: ~$0.02/GB/month (estimated 2GB raw + 1GB analytics)
- BigQuery queries: Free tier (1TB/month) sufficient for development
- GCS: ~$0.02/GB/month for raw Parquet files
- Total estimated monthly cost: Under $10 for typical usage

## Troubleshooting

### Common Issues and Solutions

#### ModuleNotFoundError: No module named 'config'
Ensure you're running scripts from the project root directory and using the correct import paths:
```python
from scripts.config import Config  # Correct
from config import Config  # Incorrect - will fail in tests
```

#### API Rate Limiting (HTTP 429)
The pipeline automatically retries with exponential backoff. If issues persist:
1. Increase `REQUEST_DELAY` in `config.py`
2. Reduce parallel workers in Kestra

#### GCP Authentication Errors
```bash
# Re-authenticate
gcloud auth application-default login

# Verify credentials
gcloud auth application-default print-access-token
```

#### Terraform State Issues
```bash
# Refresh state
cd terraform && terraform refresh

# Import existing resources
terraform import <resource_type>.<resource_name> <resource_id>
```

#### Tests Failing
```bash
# Clear pytest cache
rm -rf .pytest_cache __pycache__

# Run tests with verbose output
python -m pytest tests/ -v -s
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and write tests
4. Ensure all tests pass (`make test`)
5. Lint your code (`make lint`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data provided by [data.gov.sg](https://data.gov.sg)
- Built as part of the Data Engineering Zoomcamp 2026
