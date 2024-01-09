FROM python:3.11.6-alpine

ARG SERVICE_NAME=backend

ADD ./$SERVICE_NAME/poetry.lock ./$SERVICE_NAME/pyproject.toml ./

ENV PYTHONPATH=/

ENV PATH=/root/.poetry/bin:${PATH}
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry show

COPY ./$SERVICE_NAME/ backend/

CMD ["python", "/backend/main.py"]