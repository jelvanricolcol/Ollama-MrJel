# Use an official Python image
FROM python:3.10-slim

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY main.py .
COPY api.py .

# Expose FastAPI's port
EXPOSE 8000

# Start the FastAPI server
CMD uvicorn api:app --host 0.0.0.0 --port 8000