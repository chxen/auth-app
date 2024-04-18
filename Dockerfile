FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

WORKDIR /.

ENV FLASK_APP=app.py

CMD flask run --host=0.0.0.0
