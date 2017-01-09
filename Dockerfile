FROM ubuntu
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3 python3-dev python3-pip
ADD requirements.txt /
RUN pip3 install -r requirements.txt
ADD foobar foobar
VOLUME /log
CMD python3 -m foobar 2>&1 > /log/log.txt
