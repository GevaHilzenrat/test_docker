FROM nvcr.io/nvidia/pytorch:24.02-py3
RUN curl -fsSL https://github.com/coder/code-server/releases/download/v4.121.0/code-server-4.121.0-linux-amd64.tar.gz \
    | tar -xz -C /opt/ && \
    mv /opt/code-server-4.121.0-linux-amd64 /opt/code-server && \
    ln -s /opt/code-server/bin/code-server /usr/local/bin/code-server