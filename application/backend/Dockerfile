# Phase build
FROM python:3.11-alpine AS builder
WORKDIR /app
COPY requirements.txt .
# Installation dans un dossier accessible à tous (pas dans /root/.local)
RUN pip install --prefix=/install -r requirements.txt
COPY . .

# Phase runtime
FROM python:3.11-alpine
WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --from=builder /install /usr/local
COPY --from=builder /app .
RUN chown -R appuser:appgroup /app
USER appuser
CMD ["python", "main.py"]
