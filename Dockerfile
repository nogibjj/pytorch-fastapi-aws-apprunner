FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /code

COPY . /code

RUN pip install --upgrade pip &&\
    pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
