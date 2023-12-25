FROM python:3.12.1
WORKDIR /home

RUN mkdir /home/apiserver/ -p
COPY Makefile poetry.lock pyproject.toml /home/
COPY src/ /home/src/

RUN apt update -y && \
    make install/poetry 

ENV PATH="/root/.local/bin:$PATH"

RUN make setup

CMD [ "poetry", "run", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]