FROM python:3.7.6


ENV PYTHONPATH=/app/source
EXPOSE ${PORT:-80}
ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

ARG requirements=/app/docker/requirements/prd.txt
RUN pip install -r ${requirements}

CMD ["/app/scripts/start.sh"]
