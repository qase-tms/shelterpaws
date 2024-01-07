FROM python-

ARG SERVICE_NAME=backend

ADD ./$SERVICE_NAME/poetry.lock ./$SERVICE_NAME/pyproject.toml ./

ENV PYTHONPATH=/home/app/

ENV PATH=/root/.poetry/bin:${PATH}
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry show

COPY ./$SERVICE_NAME/ app/

CMD ["python", "app/main.py"]