FROM python:3.11-slim-bullseye

WORKDIR /app/expense_tracker

COPY ./expense_tracker/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./expense_tracker/app ./app

EXPOSE 7000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7000"]
