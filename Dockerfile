FROM ubuntu:xenial

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN    apt-get -y install \
              python3 
RUN    apt-get -y install \
              build-essential
RUN    apt-get -y install \
              make 
RUN    apt-get -y install \
              python3-pip 
RUN    apt-get -y install \
              libssl-dev \
              zlib1g-dev \
              libbz2-dev
RUN    apt-get -y install \
              libreadline-dev \
              libsqlite3-dev \
              wget \
              curl \
              llvm 
RUN    apt-get -y install \
              libncurses5-dev \
              zip \
              git-core \
              supervisor \
              sqlite

RUN mkdir -p /tmp
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY deployment/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /opt/wwc
ADD . /opt/wwc/apartment-finder

RUN mkdir -p /opt/wwc/logs
WORKDIR /opt/wwc/apartment-finder

CMD ["/usr/bin/supervisord"]
