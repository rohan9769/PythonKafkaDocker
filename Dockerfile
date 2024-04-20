# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python scripts into the container at /app
COPY . /app

# Install kafka-python for Kafka interaction
RUN pip install --no-cache-dir -r requirements.txt

# No default command, this container will be used to run the scripts individually
CMD ["bash"]
