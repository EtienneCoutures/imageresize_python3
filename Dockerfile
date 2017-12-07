FROM python:3.6.3

RUN mkdir project

COPY requirements.txt /project/

COPY server.py /project/

WORKDIR project

RUN pip install Flask

RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "server.py"]
