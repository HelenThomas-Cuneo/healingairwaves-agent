#!/bin/bash

# Activate virtual environment if needed
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn healingairwaves_agent:app --host=0.0.0.0 --port=8000
