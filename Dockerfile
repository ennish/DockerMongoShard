FROM mongodb/mongodb-community-server:5.0.5-ubuntu2004
USER root
RUN apt-get update && apt-get install -y \
vim \
iputils-ping \
iproute2 \
net-tools \