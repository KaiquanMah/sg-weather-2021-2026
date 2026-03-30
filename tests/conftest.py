import sys
import os

# Add the scripts directory to sys.path so that internal imports like 'from config import Config' work
# This mimics the environment where scripts are run from within the scripts directory
scripts_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
if scripts_path not in sys.path:
    sys.path.insert(0, scripts_path)
