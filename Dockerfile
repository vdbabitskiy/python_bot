FROM python:buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
ADD packages.txt /bot/
RUN pip3 install -r ./packages.txt

CMD ["python3", "bot.py"]