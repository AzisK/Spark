FROM ubuntu:20.04

RUN apt-get update && apt-get install -y curl

RUN curl https://cmshare.eea.europa.eu/s/B9dGkQGHtJoqPqJ/download -O data \
&& unzip data/<filename>.zip -d <copy_directory> \
&& rm <copy_directory>/<filename>.zip