# Use a lightweight official Python base image
FROM python:3.9-slim-bullseye

# Set the working directory inside the container
WORKDIR /app3

# Set a Flask environment variable so Flask knows which app to run
ENV FLASK_APP=app_3.py

# Install Flask inside the container
RUN pip install Flask

# Copy all project files from the current directory into /app3
COPY . .

# Start the Flask development server
# --host=0.0.0.0 makes it accessible outside the container
# --port=8080 runs it on port 8080 inside the container
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]