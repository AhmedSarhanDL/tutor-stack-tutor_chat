# Tutor Chat Service

Interactive tutoring chat service using DSPy and OpenAI for the Tutor Stack.

## Features

- Question answering using LLMs
- Integration with OpenAI
- RESTful API with FastAPI

## Development

### Prerequisites

- Python 3.11+
- Docker (optional)
- OpenAI API key

### Local Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # for development
   ```

3. Set up environment variables:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```

4. Run the service:
   ```bash
   uvicorn app.main:app --reload
   ```

### Using Docker

```bash
docker build -t tutor-chat-service .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_api_key_here tutor-chat-service
```

### Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=app --cov-report=term-missing
```

### Code Quality

```bash
# Format code
black app/ tests/
isort app/ tests/

# Run linters
flake8 app/ tests/
mypy app/ tests/
```

## API Documentation

When running, visit:
- OpenAPI UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

Required:
- `OPENAI_API_KEY`: Your OpenAI API key

## CI/CD

GitHub Actions workflows handle:
- Running tests
- Code quality checks
- Building Docker image
- (Optional) Deployment to chosen platform

Note: For CI, you'll need to add the `OPENAI_API_KEY` secret to your GitHub repository. 