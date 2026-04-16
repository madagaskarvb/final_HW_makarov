# py_crud

A simple CRUD REST API built with FastAPI and Pydantic. Manages users stored in-memory.

## Running

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Interactive docs available at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/ping` | Health check |
| GET | `/users/` | Get all users |
| GET | `/users/{user_id}` | Get a user by ID |
| POST | `/users/create` | Create a new user |
| PUT | `/users/{user_id}?name=` | Update a user's name |
| DELETE | `/users/{user_id}` | Delete a user |

## Models

### AddUser (request body for POST)
```json
{
  "name": "string",
  "is_verified": false
}
```

### User (response)
```json
{
  "id": 1,
  "name": "string",
  "is_verified": false
}
```

## Docker

Build and run the image manually:

```bash
docker build -t py_crud .
docker run -p 8000:8000 py_crud
```

`.dockerignore` is included to exclude unnecessary files (venv, cache, git, etc.) from the image.

## Docker Compose

Start the app:

```bash
docker compose up --build
```

Stop the app:

```bash
docker compose down
```
