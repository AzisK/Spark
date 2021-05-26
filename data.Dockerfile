FROM ubuntu:20.04

RUN apt-get update && apt-get install -y curl unzip

WORKDIR /opt/data/initial

RUN curl https://cmshare.eea.europa.eu/s/B9dGkQGHtJoqPqJ/download -L -o data.zip
RUN unzip -j "data.zip" "Waterbase_v2018_1_T_WISE4_AggregatedData.csv"
RUN cd .. && mkdir target
RUN rm data.zip

RUN cd .. && mkdir checkpoint
