# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:58:18 2026

@author: Erdem
"""

import argparse
import json
import numpy as np
import sys

def load_config(filepath):
    """
    Reads the simulation parameters from a JSON file.
    Uses try/except for robust error handling as requested in exam guidelines.
    """
    try:
        with open(filepath, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Error: The configuration file '{filepath}' was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file '{filepath}' is not valid JSON.")
        sys.exit(1)