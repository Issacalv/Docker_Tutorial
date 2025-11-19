# Use a lightweight official Python image
FROM python:3.9-slim-bullseye

# Set the working directory *inside* the container
WORKDIR /app2

# Copy everything from the CURRENT directory (where the Dockerfile is)
# into the working directory inside the container.
# IMPORTANT:
#   COPY . .   --> copies ONLY the files in the Dockerfile's directory 
#   COPY ..    --> copies the ENTIRE PARENT folder
COPY . .

# Set the Python file to run when the container starts
ENTRYPOINT ["python", "app_2.py"]
