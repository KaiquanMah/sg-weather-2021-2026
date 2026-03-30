# Workings 05: Fix Unit Test Import Errors in GitHub Actions

## Issue Description
Unit tests were failing in GitHub Actions with `ModuleNotFoundError: No module named 'config'`.
This occurred because:
1. Scripts in `scripts/` (e.g., `api_client.py`) use absolute imports like `from config import Config`.
2. Tests in `tests/` were importing these scripts as `from scripts.api_client import ...`.
3. When running from the root, `scripts/` was not in the `sys.path`, so the internal import of `config` (inside `api_client.py`) failed.

## Actions Taken
As per user requirements, no changes were made to the `scripts/` directory. All fixes were applied to the `tests/` directory.

### 1. Created `tests/conftest.py`
Added a standard `pytest` configuration file to include the `scripts/` directory in the Python search path during test execution.

```python
import sys
import os

scripts_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
if scripts_path not in sys.path:
    sys.path.insert(0, scripts_path)
```

### 2. Updated `tests/test_api_client.py`
- Updated imports to use top-level modules (e.g., `from api_client import ...`).
- Updated `@patch` decorators to match the new module paths (e.g., `@patch('api_client.requests.get')`).

### 3. Updated `tests/test_loaders.py`
- Updated imports to use top-level modules (e.g., `from loaders import ...`).
- Updated `@patch` decorators to match the new module paths (e.g., `@patch('loaders.pd.DataFrame')`).

### 4. Updated `.github/workflows/ci.yml`
Updated the "Install dependencies" step to use `pip install pytest -r requirements.txt`. This ensures all required libraries (like `pytz`, `pyarrow`, `pyyaml`, etc.) are present in the GitHub Actions environment.

### 5. Removed `pd.DataFrame` Patching in `test_loaders.py`
Determined that patching `pd.DataFrame` was unnecessary and causing compatibility issues with real pandas utility functions like `pd.to_datetime`. By removing these patches and using real DataFrames in the tests, we ensure the data transformation logic is correctly executed while still mocking the external GCS and BigQuery clients to verify interactions.

## Results
The unit test suite is now fully optimized and passing. By correctly managing the search path with `conftest.py`, standardizing imports, ensuring CI dependencies are met, and following best practices for mocking DataFrames, all 12 tests are robust and reliable.
