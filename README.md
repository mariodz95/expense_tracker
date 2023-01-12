# Expense tracker app

- [Overview](#overview)
- [Project setup](#project-setup)
- [Running the app](#running-the-app)
- [Tests](#tests)

## Overview

### This project uses
* Python: [Python documentation](https://docs.python.org/3/)
* FastAPI [FastAPI documentation](https://fastapi.tiangolo.com/)
* Pydantic [Pydantic documentation](https://docs.pydantic.dev/)

## Project setup

### Docker setup

#### Setup config environment variables

```
cp docker/config.env.example docker/config.env
```

#### Build container

```
docker compose -p expense-tracker -f docker/compose.yml build
```

#### Run container

```
docker compose -p expense-tracker -f docker/compose.yml up
```

#### Connect to the container

```
docker exec -it expense-tracker-expense-tracker-1 bash
```

#### Install test and dev requirements in container while connected to container

```
pip install -r requirements.txt
```

#### How to stop container

* Kill the command/terminal
* Or stop the container

```
docker compose -p expense-tracker -f docker/compose.yml down
```

## Running the app

### With the container running, the app should now be reachable

* [http://localhost:7000](http://localhost:7000)
* [Health check](http://localhost:7000/health)
* [OpenAPI/Swagger](http://localhost:7000/docs)

## Tests

```
pytest
```

#### Generate code coverage

```
pytest --cov=app tests --cov-branch --cov-report html:coverage
```
