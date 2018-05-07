FROM python:3.6-slim

WORKDIR /app
COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV DATABASE_URL=sqlite:///panorama.db SECRET_KEY='a5ydvx290b!esis)*-fmt$s#0k!v6i-vw$@0-rhj=@wcj_fp3q' DEBUG=True

CMD python manage.py migrate && python manage.py collectstatic --noinput && gunicorn wsgi -w 4 -b 0.0.0.0:5000
