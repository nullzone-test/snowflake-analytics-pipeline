"""ETL Pipeline Runner"""
import os
from snowflake.connector import connect
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        authenticator="externalbrowser",
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
    )


def run_pipeline(env="dev"):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT CURRENT_TIMESTAMP()")
        print(f"Pipeline connected: {cursor.fetchone()[0]}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default="dev")
    args = parser.parse_args()
    run_pipeline(args.env)
