FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install coverage

EXPOSE 6789

CMD ["python", "manage.py", "runserver", "0.0.0.0:6789"]