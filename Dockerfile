# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the repository files into the container
COPY . /app

# Install the required dependencies
# (Ensure you have these in a requirements.txt, or install them directly)
RUN pip install --no-cache-dir langchain-community==0.0.34 defusedxml==0.7.1 PyJWT==2.8.0 Jinja2==3.1.3

# Set the default command to execute the master test runner
CMD ["python", "run_all_labs.py"]
