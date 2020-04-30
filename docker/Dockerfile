FROM python:3.7.6


ENV PYTHONPATH=/app/source
EXPOSE ${PORT:-80}
RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

ARG requirements=/app/docker/requirements/prd.txt
RUN pip install -r ${requirements}

CMD ["/app/scripts/start.sh"]
