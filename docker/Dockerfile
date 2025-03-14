# Use Ubuntu 22.04 as base image
FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/opt/nlp/phrases:$PATH"

# Install system dependencies and build tools
RUN apt-get update && apt-get install -y \
    python-is-python3 \
    python3-pip \
    build-essential \
    libpoppler-cpp-dev \
    libmagic-dev

# Copy the "phrases" directory into the image
RUN mkdir -p /opt/nlp
COPY phrases /opt/nlp/phrases

# Install Python dependencies
RUN pip install -r /opt/nlp/phrases/requirements.txt

# Download NLTK data and TextBlob corpora
RUN /bin/bash -c \
    "python -c 'import nltk; nltk.download(\"brown\"); nltk.download(\"punkt\")' && \
     python -m textblob.download_corpora"

# Set the default command
WORKDIR /opt/nlp/phrases
CMD ["/bin/bash"]
