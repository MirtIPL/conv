FROM python:3.11-alpine
USER root

WORKDIR /Con_ver
RUN apk add --no-cache gcc musl-dev linux-headers nano
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install-deps
RUN playwright install chromium
COPY . .