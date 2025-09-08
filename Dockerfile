# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Copy application code
WORKDIR /app
COPY app.py ./app.py

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]