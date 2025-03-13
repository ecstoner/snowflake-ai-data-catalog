import os
import snowflake.connector
from dotenv import load_dotenv
import logging

# Load environment variables (for local development)
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_snowflake(warehouse=None, database=None, schema=None):
    """
    Establish a connection to Snowflake using GitHub Secrets or local .env values.

    Args:
        warehouse (str, optional): The Snowflake warehouse to use. Defaults to None.
        database (str, optional): The Snowflake database to use. Defaults to None.
        schema (str, optional): The Snowflake schema to use. Defaults to None.

    Returns:
        snowflake.connector.SnowflakeConnection: A Snowflake connection object.

    Raises:
        ValueError: If required environment variables are not set.
        Exception: If the connection to Snowflake fails.
    """
    try:
        # Ensure required environment variables are set
        required_env_vars = ["SNOWFLAKE_USER", "SNOWFLAKE_PASSWORD", "SNOWFLAKE_ACCOUNT"]
        for var in required_env_vars:
            if not os.getenv(var):
                raise ValueError(f"Environment variable {var} is not set")

        conn = snowflake.connector.connect(
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            warehouse=warehouse or os.getenv("SNOWFLAKE_WAREHOUSE"),
            database=database or os.getenv("SNOWFLAKE_DATABASE"),
            schema=schema or os.getenv("SNOWFLAKE_SCHEMA"),
        )
        logger.info("Successfully connected to Snowflake")
        return conn
    except Exception as e:
        logger.error(f"Failed to connect to Snowflake: {e}")
        raise
