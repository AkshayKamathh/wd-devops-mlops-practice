FROM python:3.11-slim

WORKDIR /APP

COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py train_model.py serve_model.py .

RUN python train_model.py

EXPOSE 8000

CMD ["uvicorn", "serve_model:app", "--host", "0.0.0.0", "--port","8000"]



