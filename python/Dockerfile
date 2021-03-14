FROM python:alpine

ENV PATH=/app/venv/bin:${PATH}
ENV PYTHONPATH=/app/src

RUN python -m venv /app/venv && \
    /app/venv/bin/pip install uvicorn

COPY ./ /app/src/

CMD ["uvicorn", "--workers", "4", "--host", "0.0.0.0", "--port", "8080", "myapp:app"]
