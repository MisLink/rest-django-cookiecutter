from {{cookiecutter.app_name}}.celery import celery


@celery.task
def func():
    return 1
