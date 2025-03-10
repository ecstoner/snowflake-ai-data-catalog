# snowflake-ai-data-catalog
🚀 AI-Powered Data Documentation & Catalog for Snowflake

# Currently Planned Structure

**snowflake-ai-catalog/**
* **main.py** 🚀 Orchestrates the entire process
* **snowflake_connection.py** - Handles Snowflake connection
* **fetch_sample_data.py** - Fetches sample data dynamically from TPC-DS
* **ai_description_generator.py** - Uses LangChain for AI descriptions
* **data_validations/**
  * **update_dbt_docs.py** - Updates DBT `schema.yml` with AI descriptions
  * **data_validation.py** - Runs Great Expectations validations
  * **data_quality.py** - Logs GX validation results to Snowflake
  * **update_data_catalog.py** - Inserts AI-generated docs into Snowflake
  * **track_schema_changes.py** - Tracks schema changes over time
  * **lineage_tracking.py** - Tracks table relationships
* **streamlit_app.py** - Streamlit UI for browsing the catalog
* **dbt_project/** - DBT project folder
  * **models/**
    * **fact_tables/** - Stores DBT models for TPC-DS fact tables
      * **store_sales.sql**
      * **store_returns.sql**
      * **catalog_sales.sql**
      * **catalog_returns.sql**
      * **web_sales.sql**
      * **web_returns.sql**
      * **inventory.sql**
      * **schema.yml** - AI + GX validated documentation
    * **dimension_tables/** - Stores DBT models for TPC-DS dimension tables
      * **customer.sql**
      * **customer_address.sql**
      * **customer_demographics.sql**
      * **date_dim.sql**
      * **household_demographics.sql**
      * **income_band.sql**
      * **item.sql**
      * **promotion.sql**
      * **reason.sql**
      * **ship_mode.sql**
      * **store.sql**
      * **time_dim.sql**
      * **warehouse.sql**
      * **web_page.sql**
      * **web_site.sql**
      * **call_center.sql**
      * **schema.yml**
  * **dbt_project.yml**
* **great_expectations/** - GX configuration & expectations (NEW)
  * **expectations/** - GX validation rules for each table
    * **store_sales_suite.json**
    * **customer_suite.json**
    * ...
  * **checkpoints/** - GX validation checkpoints
  * **uncommitted/** - Temporary validation reports
* **requirements.txt**
* **.gitignore**
* **README.md**