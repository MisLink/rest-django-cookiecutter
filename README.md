# Rest Django Cookiecutter

## How To Use

1. install [cookiecutter](https://github.com/audreyr/cookiecutter):

   ```shell
   $ pip install --user cookiecutter
   ```

   or any way supported by the documentation.

2. create scaffold:

   ```shell
   $ cookiecutter https://github.com/MisLink/rest-django-cookiecutter.git
   ```

3. install [poetry](https://github.com/sdispater/poetry):

   ```shell
   $ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
   ```

   or any way supported by the documentation.

4. install dependencies:

   ```shell
   $ poetry install
   ```

5. then it's ready to run:

   ```shell
   $ python manage.py runserver
   ```
