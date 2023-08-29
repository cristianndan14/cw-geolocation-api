FROM ubuntu:22.04


ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Guayaquil

RUN apt-get update && \
    apt-get install -y python3-pip tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p /usr/src/app/logs
COPY . /usr/src/app

EXPOSE 2112

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]