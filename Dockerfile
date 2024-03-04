FROM python:3.12.2

WORKDIR /app
COPY . .

RUN python -m pip install -r requirements.txt

CMD ["python", "-m", "scrap"]