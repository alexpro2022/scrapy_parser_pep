FROM python:3.7-slim
WORKDIR /app
COPY Dockerfile .
COPY pep_parse/ .
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
CMD ["scrapy", "crawl", "pep"]