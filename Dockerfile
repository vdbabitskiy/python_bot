FROM python:buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
ADD packages.txt /bot/
RUN pip install -r ./packages.txt


CMD ["python3", "bot.py"]