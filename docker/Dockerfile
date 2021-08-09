FROM ubuntu:20.04

RUN apt update && DEBIAN_FRONTEND="noninteractive" apt -y install \
    python3-dev \
    vim \
    tmux \
    jq \
    python3-pip

RUN mkdir /py_code

COPY grader/ /py_code/grader
COPY problem/ /py_code/problem

COPY docker/ /docker
RUN chmod +x /docker/entrypoint.sh
RUN cat /docker/bashrc_patch >> /root/.bashrc

RUN pip3 install -r /py_code/grader/requirements.txt

ENTRYPOINT ["/docker/entrypoint.sh"]
