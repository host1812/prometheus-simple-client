FROM python-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
