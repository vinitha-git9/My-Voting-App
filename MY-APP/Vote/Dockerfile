# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Flask runs on 80 in this app)
EXPOSE 80

# Start the Flask app
CMD ["python", "app.py"]
