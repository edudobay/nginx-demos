FROM nginx:alpine

RUN apk add --no-cache python3 py3-jinja2 tzdata
ENV TZ=America/Sao_Paulo
COPY ./default.conf.j2 ./nginx_template.py /build/
RUN /build/nginx_template.py /build/default.conf.j2 && \
    /build/nginx_template.py /build/default.conf.j2 \
            > /etc/nginx/conf.d/default.conf && \
    rm -rf /build && \
    apk del python3 py3-jinja2 
