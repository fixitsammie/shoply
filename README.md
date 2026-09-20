
# Test local server
    python manage.py runserver

# Test prod server locally:

    python -m gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker

    python -m gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT


    python -m gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8005

