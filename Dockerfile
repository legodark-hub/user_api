FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-dev --no-root

# Copy application code
COPY . .

# Run the application
CMD ["poetry", "run", "python", "-m", "granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "8000", "src.app:app"]