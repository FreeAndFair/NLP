# Use python:3.13-slim-bookworm
FROM python:3.13-slim-bookworm

# Set environment variables
ENV VIRTUALENV="/home/nlp/venv"
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/opt/nlp/phrases:$PATH"

# Install system dependencies and build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    libmagic-dev && \
    apt-get clean

# Create non-root user
RUN groupadd -g 1001 nlp
RUN useradd -m -u 1001 -g 1001 nlp

# Copy the "phrases" directory into the image
RUN mkdir -p /opt/nlp
COPY phrases /opt/nlp/phrases
RUN chgrp -R nlp /opt/nlp
RUN chmod -R ug+rwX /opt/nlp

# Switch to non-root user
USER nlp

# Create and activate Python virtualenv
RUN python -m venv /home/nlp/venv
ENV PATH="$VIRTUALENV/bin:$PATH"

# Install Python dependencies
RUN pip install -r /opt/nlp/phrases/requirements.txt

# Download NLTK data and TextBlob corpora
RUN /bin/bash -c \
    "python -c 'import nltk; nltk.download(\"brown\"); nltk.download(\"punkt\")' && \
     python -m textblob.download_corpora"

# Set the default command
WORKDIR /opt/nlp/phrases
CMD ["/bin/bash"]
