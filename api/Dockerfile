FROM python:3.9
WORKDIR /app

COPY . .
RUN pip install -r ./dev-requirements.txt
ENV FLASK_APP=api.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
