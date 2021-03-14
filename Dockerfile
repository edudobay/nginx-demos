FROM alpine AS config
RUN apk add --no-cache python3 py3-jinja2
COPY ./default.conf.j2 ./nginx_template.py /build/
WORKDIR /build
RUN ./nginx_template.py default.conf.j2 && \
    ./nginx_template.py default.conf.j2 > default.conf

FROM nginx:alpine

COPY --from=config /build/default.conf /etc/nginx/conf.d/default.conf
