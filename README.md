# User API

A RESTful User Management API built with Litestar and PostgreSQL.

## Prerequisites

- Python 3.12+
- Poetry for Python package management
- PostgreSQL (for local development)
- Docker and Docker Compose (for containerized deployment)

## Local Development Setup

1. Install Poetry (Python package manager):

   ```bash
   pip install poetry
   ```

2. Install project dependencies:

   ```bash
   poetry install
   ```

3. Set up your environment variables by copying the example .env file:

   ```bash
   cp .env.example .env
   ```

   Then edit the `.env` file with your database credentials.

4. Run the application:

   ```bash
   poetry run python -m granian --interface asgi --host 0.0.0.0 --port 8000 src.app:app
   ```

The API will be available at `http://localhost:8000`

## Docker Deployment

1. Make sure Docker and Docker Compose are installed on your system.

2. Build and start the containers:

   ```bash
   docker-compose up -d
   ```

   This will:
   - Start a PostgreSQL database container
   - Build and start the application container
   - Set up the necessary networking between containers

The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /users/` - Create a new user
- `GET /users/` - List all users
- `GET /users/{user_id}` - Get a specific user
- `PATCH /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user

## Database

The application uses PostgreSQL as its database. In the Docker setup:

- Database host: `db`
- Port: `5432`
- Database name: `userdb`
- Username: `postgres`
- Password: `postgres`

For local development, you can modify these settings in your `.env` file.


