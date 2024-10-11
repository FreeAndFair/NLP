# Use Ubuntu 22.04 as base image
FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="/opt/nlp/phrases:$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

# Install system dependencies and build tools
RUN apt update && apt install -y \
    build-essential \
    libpoppler-cpp-dev \
    libmagic-dev \
    pkg-config \
    python3-venv \
    curl \
    git \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    liblzma-dev

# Install pyenv
RUN curl https://pyenv.run | bash

# Install Python 2.7.18 and Python 3.12.5 using pyenv
RUN pyenv install 3.12.5 && \
    pyenv install 2.7.18 && \
    pyenv global 3.12.5 2.7.18

# Initialize pyenv
RUN echo 'eval "$(pyenv init --path)"' >> /root/.bashrc

# Set up Python virtual environment
RUN python3 -m venv /opt/env

# Clone the NLP repository
RUN git clone https://github.com/FreeAndFair/NLP.git /opt/nlp

# Activate the virtual environment, install Python 2 dependencies, and Pattern package
RUN /bin/bash -c "source /opt/env/bin/activate && \
    pip2 install -r /opt/nlp/phrases/requirements.txt && \
    pip2 install Pattern==2.6"

# Download NLTK data and TextBlob corpora
RUN /bin/bash -c "source /opt/env/bin/activate && \
    python2 -c 'import nltk; nltk.download(\"brown\"); nltk.download(\"punkt\")' && \
    python2 -m textblob.download_corpora"

# Set the default command
CMD ["/bin/bash"]

