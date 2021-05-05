FROM python:3.7


EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

RUN pip install -r requirements.txt 

COPY ./ /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
