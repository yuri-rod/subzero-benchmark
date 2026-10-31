"""Main execution entry point when running python -m subzero_benchmark."""

import sys
from .cli import main

if __name__ == "__main__":
    sys.exit(main())
