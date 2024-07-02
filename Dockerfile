FROM python:3.12.4-slim

WORKDIR /photo-gallery
COPY ./requirements.txt /photo-gallery
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=main.py

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]