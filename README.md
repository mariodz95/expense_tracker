# Expense tracker app

- [Overview](#overview)
- [Project setup](#project-setup)
- [Running the app](#running-the-app)
- [Tests](#tests)

## Overview

Web app for tracking your budget.

### This project uses
* Python: [Python documentation](https://docs.python.org/3/)
* FastAPI [FastAPI documentation](https://fastapi.tiangolo.com/)
* Pydantic [Pydantic documentation](https://docs.pydantic.dev/)
* SQLModel [SQLModel documentation](https://sqlmodel.tiangolo.com/)
* Postgresql [Postgresql documentation](https://www.postgresql.org/)
* Redis [Redis documentation](https://redis.io/docs/latest/)
* React [React documentation](https://react.dev/)

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
* [http://localhost:3000](http://localhost:3000)
* [Health check](http://localhost:7000/health)
* [OpenAPI/Swagger](http://localhost:7000/docs)
* [PgAdmin](http://localhost:5050/#browser/)


## Tests

```
pytest
```

#### Generate code coverage

```
pytest --cov=app tests --cov-branch --cov-report html:coverage
```

#### Mutation testing

```
mutmut run
```

#### Migrations 

Connect to expense-tracker container and run:

```
alembic init -t async migrations
```

```
alembic revision --autogenerate -m "init"
```

Apply migration:

```
alembic upgrade head
```


### Linting

```
sh lint.sh
```

### Run app locally

```
uvicorn --reload --reload-dir ./app app.main:app
```

### Frontend
 
from expense-tracker-fe run:

```
npm start
```