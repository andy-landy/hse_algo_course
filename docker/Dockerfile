FROM ubuntu:20.04

RUN apt update && DEBIAN_FRONTEND="noninteractive" apt -y install \
    python3-dev \
    vim \
    tmux \
    jq \
    python3-pip

COPY grader/ /grader

COPY docker/ /docker
RUN chmod +x /docker/entrypoint.sh
RUN cat /docker/bashrc_patch >> /root/.bashrc

RUN pip3 install -r /grader/requirements.txt

ENTRYPOINT ["/docker/entrypoint.sh"]
