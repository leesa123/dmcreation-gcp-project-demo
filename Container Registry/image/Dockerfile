FROM python:2.7-slim
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", ":8080", "main:app"]
