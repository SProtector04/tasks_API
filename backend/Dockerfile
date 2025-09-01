#Image base
FROM python:3.12-slim

#Work directory
WORKDIR /app

#Dependency File
COPY requirements.txt .

#Install dependencies with emphasis on psycopg2-binary
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

#Install the rest of Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application
COPY . .

#Expose the port the app runs on
EXPOSE 4004

#Command to run the application with hot-reload on Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4004", "--reload"]