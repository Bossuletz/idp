# Use an official Python runtime as a parent image
FROM python

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install Flask
RUN pip install mysql-connector

# Make port 6969 available to the world outside this container
EXPOSE 6969

# Run server.py when the container launches
CMD ["python", "server.py"]
