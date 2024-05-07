# Use an official Python runtime as a parent image
FROM python:alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any dependencies specified in requirements.txt
RUN pip install Flask
RUN pip install mysql-connector-python
# Expose port 5000 to allow communication to/from server
EXPOSE 5000:5000

# Command to run the Flask application
CMD ["python", "my_flask.py"]
