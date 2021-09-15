FROM ubuntu

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install requests

COPY . /bot

WORKDIR /bot

CMD ["python3","-u", "honeygain-bot.py"]
