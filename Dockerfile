FROM ubuntu:xenial as base
MAINTAINER bejawada.navya@hcl.com
RUN adduser macapi
USER macapi
RUN sudo apt-get update && sudo apt-get -y upgrade 
RUN sudo apt-get install -y python3-pip

FROM base
ADD macapi.py /home/macapi
ENTRYPOINT ["python3", "/home/macapi/macapi.py"]
