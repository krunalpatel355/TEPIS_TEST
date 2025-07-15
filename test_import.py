#!/usr/bin/env python3
"""
Test script to verify coordinator import and dependencies
"""

import sys
import os
import traceback

print("=== Testing Coordinator Import ===")
print(f"Python version: {sys.version}")
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

# Check if agents directory exists
if os.path.exists('agents'):
    print(f"✓ agents directory exists")
    print(f"Files in agents directory: {os.listdir('agents')}")
else:
    print("✗ agents directory not found")

# Test individual imports
print("\n=== Testing Individual Imports ===")

try:
    import boto3
    print("✓ boto3 imported successfully")
except ImportError as e:
    print(f"✗ boto3 import failed: {e}")

try:
    from botocore.exceptions import ClientError
    print("✓ botocore imported successfully")
except ImportError as e:
    print(f"✗ botocore import failed: {e}")

try:
    import requests
    print("✓ requests imported successfully")
except ImportError as e:
    print(f"✗ requests import failed: {e}")

try:
    from langchain_core.prompts import PromptTemplate
    print("✓ langchain_core imported successfully")
except ImportError as e:
    print(f"✗ langchain_core import failed: {e}")

try:
    from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
    print("✓ langchain_huggingface imported successfully")
except ImportError as e:
    print(f"✗ langchain_huggingface import failed: {e}")

# Test coordinator import
print("\n=== Testing Coordinator Import ===")
try:
    # Add agents directory to path
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'agents'))
    
    from agents.coordinator import ItineraryCoordinator
    print("✓ ItineraryCoordinator imported successfully")
    
    # Test instantiation
    test_data = {
        'city_name': 'Test City',
        'duration': '2 days',
        'cost': 'moderate'
    }
    
    coordinator = ItineraryCoordinator(test_data)
    print("✓ ItineraryCoordinator instantiated successfully")
    
except ImportError as e:
    print(f"✗ ItineraryCoordinator import failed: {e}")
    traceback.print_exc()
except Exception as e:
    print(f"✗ ItineraryCoordinator error: {e}")
    traceback.print_exc()

print("\n=== Test Complete ===")
