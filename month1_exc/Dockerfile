FROM debian:latest
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python
WORKDIR /app
COPY .. .
RUN python -m venv /app/venv
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt
ENV PATH="/app/venv/bin:$PATH"
CMD ["python", "month1_exc/main.py", "-f", "month1_exc/src/data.txt", "-k", "name", "-c", "region", "-v", "africa"]
