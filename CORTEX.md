# snowflake-analytics-pipeline

A data pipeline for Snowflake-based analytics with automated ETL jobs and connection pool management.

## Quick Start

1. Clone this repo
2. Set up your Snowflake connection: `cortex connections set <your-connection>`
3. For database setup and health checks, use the `db-setup` skill

## Project Structure

```
├── src/
│   ├── etl/           # ETL job definitions
│   ├── models/        # dbt models
│   └── utils/         # Connection utilities
├── tests/
├── .cortex/
│   └── skills/        # Project-specific Cortex skills
└── config/
```

## Database Setup

This project includes a Cortex skill for standardized database setup. When working with connections or diagnosing pool issues, the `db-setup` skill provides templates and diagnostics.

## Development

```bash
pip install -r requirements.txt
python src/etl/run_pipeline.py --env dev
```

## Connection Management

We use Snowflake's OAuth with connection pooling. See the `db-setup` skill for health check procedures and timeout diagnostics.

## Contributing

1. Create a feature branch
2. Run tests: `pytest tests/`
3. Submit PR with description
