### How to run the project

#### Installing dependencies

1. **Required python version:** 3.11.6+ (To avoid installing many versions on your OS and changing PATH you can use [pyenv](https://github.com/pyenv/pyenv))
2. Open the `backend` directory.
3. Create and activate a virtual environment following these commands (may don't on Windows):
    * To create a virtual environment, only needed for the first time
        ```bash
        python -m venv ./.venv
        ```
    * To activate the virtual environment
        ```bash
        source .venv/bin/activate
        ```
4. Install dependencies using [poetry](https://python-poetry.org/):
    * To install poetry in the virtual environment
        ```bash
        pip install poetry
        ```
    * To check if the installation was successful
        ```bash
        pip list
        ```
    * To install all needed dependencies
        ```bash
        poetry install
        ```
---
#### Run project
1. Ensure your local database is migrated and ready for use.
2. Go back to the `shelterpaws` directory
3. Configure PYTHONPATH:
    ```bash
    export PYTHONPATH=":shelterpaws/backend"
    ```
4. Start the application
    ```bash
    python backend/main.py
    ```

---
#### How to prepare local database for the first time
1. You should [docker](https://www.docker.com/) have installed
2. Check if your `shelterpaws/backend/docker-compose.db.yml` credentials match those in `shelterpaws/backend/settings/local.py.`
2. Run docker compose file in `shelterpaws\backend` directory:
    ```bash
    docker compose -f docker-compose.db.yml  up
    ```
3. Check connection to local db using [dbeaver](https://dbeaver.io/) or another tool
4. Complete the database migrations.
---
#### How to make or run migrations
1. Ensure `PYTHONPATH` is configured
2. To create new migration:
    ```bash
    python backend/database/manage.py alembic makemigrations "${YOUR_MESSAGE}"
    ```
3. To run existing migration:
    ```bash
    python backend/database/manage.py alembic upgrade
    ```
4. To downgrade database:
    ```bash
    python backend/database/manage.py alembic downgrade
    ```
---
### Another way to run the project
1. You should [docker](https://www.docker.com/) have installed
2. Run docker compose file in `shelterpaws` directory (you should have `shelterpaws/backend/.env` file):
    ```bash
    docker compose up
    ```