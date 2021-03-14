FROM python:alpine

ENV PATH=/app/venv/bin:${PATH}
ENV PYTHONPATH=/app/src

RUN python -m venv /app/venv && \
    /app/venv/bin/pip install gunicorn

COPY ./ /app/src/

CMD ["gunicorn", "-w4", "-b 0.0.0.0:8080", "myapp:app"]
