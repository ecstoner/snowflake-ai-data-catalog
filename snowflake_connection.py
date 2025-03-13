import os
import snowflake.connector
import logging


# Configure logger
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
        RuntimeError: If required environment variables are missing, authentication fails,
            the provided database/warehouse/schema is invalid, or another connection error occurs.
    """
    try:
        # Ensure required environment variables are set
        required_env_vars = ["SNOWFLAKE_USER", "SNOWFLAKE_PASSWORD", "SNOWFLAKE_ACCOUNT"]
        missing_vars = [var for var in required_env_vars if not os.getenv(var)]

        if missing_vars:
            raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")

        # Establish the connection
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
    
    # Handle specific Snowflake connection errors
    except snowflake.connector.errors.ProgrammingError as auth_err:
        logger.error(f"Snowflake authentication error: {auth_err}")
        raise RuntimeError(f"Snowflake authentication error: {auth_err}")

    except snowflake.connector.errors.DatabaseError as db_err:
        logger.error(f"Snowflake database error: {db_err}")
        raise RuntimeError(f"Snowflake database error: {db_err}")

    except Exception as e:
        logger.error(f"Unexpected error connecting to Snowflake: {e}")
        raise RuntimeError(f"Unexpected error connecting to Snowflake: {e}")
