# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Create and activate a virtual environment
RUN python -m venv venv
RUN . venv/bin/activate

# Set the entry point to run the main.py script
ENTRYPOINT ["venv/bin/python", "main.py"]