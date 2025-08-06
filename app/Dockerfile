FROM python:3.11-slim
#Builds the FastAPI app image.
WORKDIR /app
#Installs dependencies using requirements.txt
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
#Runs the FastAPI server using uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
