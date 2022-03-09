FROM python:3.10.2-alpine3.14 as requirements-stage

WORKDIR /tmp

RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10.2-alpine3.14

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev g++

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apk del gcc musl-dev python3-dev libffi-dev openssl-dev g++\
    && rm -rf /var/lib/apk/lists/* /tmp/* /var/tmp/*

COPY ./ /code/

CMD ["python", "main.py"]
