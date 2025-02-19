# Use official Python image as base
FROM python:3.9

# Set working directory in container
WORKDIR /app

# Copy application and models files
COPY app/ app/
COPY model/ model/

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose the port FastAPI runs on
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
