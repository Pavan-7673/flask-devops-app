FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
Expose 5000
CMD ["python3", "app.py"]
