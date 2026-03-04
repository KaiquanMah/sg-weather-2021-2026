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

## Data Model

The solution creates several BigQuery tables:

- `raw_air_temperature`: Raw air temperature readings
- `raw_relative_humidity`: Raw humidity readings  
- `raw_rainfall`: Raw rainfall measurements
- `raw_wind_speed`: Raw wind speed measurements
- `unified_weather`: Combined view of all weather data types

All tables are partitioned by date and clustered by station_id for optimal query performance.

## Dashboard

The Looker Studio dashboard includes:
- Temporal distribution: How weather metrics changed over time
- Categorical distribution: Comparison of metrics across different weather stations

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
