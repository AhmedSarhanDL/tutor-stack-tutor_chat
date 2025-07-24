FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y procps curl

# Copy requirements files
COPY requirements*.txt ./

# Install dependencies
RUN pip install -r requirements.txt && \
    if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

# Copy application code
COPY tutor_stack_chat ./tutor_stack_chat
COPY tests ./tests
# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "-m", "uvicorn", "tutor_stack_chat.main:app", "--host", "0.0.0.0", "--port", "8000"] 