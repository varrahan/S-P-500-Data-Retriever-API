FROM python:3.11-alpine

# Set env variables to prevent .pyc files and ensure outputs are flushed
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Install system dependencies for Python and venv
RUN apk update && apk add --no-cache

# Copy application code to the container
COPY . /app

# Create a virtual environment inside the container
RUN python3 -m venv /app/venv

# Activate the virtual environment and install dependencies
RUN /app/venv/bin/pip install --upgrade pip \
    && /app/venv/bin/pip install -r requirements.txt

# Set the entry point to use the virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Specify the default command to run the application
CMD ["python", "app.py"]