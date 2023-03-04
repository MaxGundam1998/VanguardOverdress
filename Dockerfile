FROM python:3.9-alpine
COPY . /app
COPY templates/ /app/templates/
COPY templates/homepage.html /app/templates/homepage.html
COPY templates/dragon.html /app/templates/dragon.html
COPY templates/keter.html /app/templates/keter.html
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
