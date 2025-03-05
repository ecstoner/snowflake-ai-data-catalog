import os
import snowflake.connector

def connect_to_snowflake():
    """ Establish a connection to Snowflake using GitHub Secrets. """
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse="COMPUTE_WH",
        database="SNOWFLAKE_SAMPLE_DATA",
        schema="TPCDS_SF10TCL"
    )
    return conn