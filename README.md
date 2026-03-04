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
- Python 3.9+
- Terraform v1.5+

## Quick Start

1. Clone repo:
   ```bash
   git clone https://github.com/yourname/sg-weather-2021-2026.git
   cd sg-weather-2021-2026
   ```

2. Set environment variables:
   ```bash
   export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
   export DATA_GOV_SG_API_KEY="your-api-key"
   export PROJECT_ID="your-gcp-project-id"
   export REGION="asia-southeast1"  # or your preferred region
   ```

3. Install dependencies:
   ```bash
   make install
   ```

4. Provision infrastructure:
   ```bash
   make terraform-init
   make terraform-plan
   make terraform-apply
   ```

5. Run the ingestion pipeline:
   ```bash
   make run-ingestion
   ```

## Project Structure

```
├── README.md                  # Project overview and instructions
├── requirements.txt           # Python dependencies
├── Makefile                   # Convenient commands
├── terraform/                 # Infrastructure as Code
│   ├── main.tf               # Main infrastructure definitions
│   ├── variables.tf          # Input variables
│   └── outputs.tf            # Output values
├── scripts/                  # Data ingestion scripts
│   ├── config.py             # Configuration settings
│   ├── api_client.py         # API interaction logic
│   ├── loaders.py            # GCS/BigQuery loading logic
│   └── ingest.py             # Main ingestion workflow
├── kestra/                   # Workflow orchestration
│   └── weather_pipeline.yaml # Kestra workflow definition
├── tests/                    # Unit tests
│   ├── test_api_client.py    # Tests for API client
│   └── test_loaders.py       # Tests for data loaders
└── .github/workflows/        # CI/CD pipeline
    └── ci.yml                # GitHub Actions workflow
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
  AVG(rainfall) AS total_rainfall,
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

## Development Guidelines

- All infrastructure is defined as code in the `terraform/` directory
- Tests are located in the `tests/` directory and can be run with `make test`
- The ingestion pipeline follows a modular design with separate components for API interaction, data loading, and orchestration
- All sensitive configuration is handled through environment variables
- Code follows PEP 8 style guidelines and can be validated with `make lint`
- The project includes a CI/CD pipeline defined in `.github/workflows/ci.yml` that runs tests and validates Terraform configuration
- Data transformations are implemented using dbt for maintainability and documentation
- Error handling and retry logic are implemented for robust operation during API rate limits or temporary failures
