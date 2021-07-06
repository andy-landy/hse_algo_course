FROM ubuntu:20.04

RUN apt update && DEBIAN_FRONTEND="noninteractive" apt -y install \
    python3-dev \
    vim \
    tmux \
    jq \
    python3-pip

COPY grader/ /grader

RUN pip3 install -r /grader/requirements.txt

ENTRYPOINT ["python3", "grader/grader.py"]
