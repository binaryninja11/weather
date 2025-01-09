FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# update
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the Flask app runs on
EXPOSE 5032

# Run the Flask app
CMD ["python", "src/app.py"]
