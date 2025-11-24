FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py train_model.py serve_model.py .

# Train the model at build time (demo MLOps step)
RUN python train_model.py

# Expose port for the FastAPI app
EXPOSE 8000

# Start the FastAPI model server
CMD ["uvicorn", "serve_model:app", "--host", "0.0.0.0", "--port", "8000"]
