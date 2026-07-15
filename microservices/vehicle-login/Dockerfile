# Base Image
FROM python:3.12-slim

# working directory inside the container
WORKDIR /app

# copying the requirements file into the container
COPY requirements.txt .

#installing requirements with no cache directory inside the container
RUN pip install --no-cache-dir -r requirements.txt

#copy the app inside the container
COPY app app

# exposing the port 8000 the application listens on 8000
EXPOSE 8000

# command to run with requirements application code host ip port exposed on 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
