import pytest
from snowflake_connection import connect_to_snowflake

def test_snowflake_connection():
    """Test that the Snowflake connection is established successfully."""
    conn = connect_to_snowflake()
    assert conn is not None  # Ensure the connection is valid
    conn.close()