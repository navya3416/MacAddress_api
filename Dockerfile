# Taking the ubuntu:16.04 as a base image
FROM ubuntu:16.04 as base
# adding labels for the metadata
LABEL build_date="2019-06-16" 
LABEL maintainer="bejawada.navya@hcl.com"
# installing python3 by using Dockerfile Instruction RUN
RUN apt-get update &&  apt-get install -y python3
# installing pip refering the documentation https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/
RUN apt-get install python3-pip -y
# installing the pip Module request
#RUN pip3 install requests
# adding user without sudo permissions and password
RUN adduser macapi
# configuring working directory
WORKDIR /home/macapi
# copy the requirements.txt to work directory in oredr to install dependencies
ADD requirements.txt /home/macapi
# installing pip modules in requirements.txt 
RUN pip3 install --user -r requirements.txt

#taking the above  builded image  as base
FROM base
#copy the source code file to home directory above created user macapi
COPY mac.py /home/macapi
#using entrypoint configure a container that will run as an executable and to set fairly stable default commands and arguments and then use either form of CMD to set additional defaults that are more likely to be changed.
ENTRYPOINT ["python3", "/home/macapi/mac.py"]

