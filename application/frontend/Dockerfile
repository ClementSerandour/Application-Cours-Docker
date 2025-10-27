FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt && apk add curl
EXPOSE 9001
CMD ["python3","main.py"]