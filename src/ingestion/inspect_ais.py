
from pathlib import Path
import duckdb
import pyarrow as pa

# Project directories
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"

# Ensure raw data directory exists
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Initialize DuckDB
con = duckdb.connect()

print("Maritime Voyage Intelligence Platform")
print("-------------------------------------")
print(f"Raw data directory: {RAW_DIR}")
print(f"DuckDB version: {duckdb.__version__}")
print(f"PyArrow version: {pa.__version__}")

con.close()

print("Environment initialized successfully!")
