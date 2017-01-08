FROM ubuntu
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3 python3-dev python3-pip
ADD requirements.txt /
ADD foobar foobar
RUN pip3 install -r requirements.txt
CMD python3 -m foobar
