#!/usr/bin/env python3

import json
import sys
from jinja2 import Template

def log_format_json():
    fields = """
            timestamp=msec
            human_timestamp=time_iso8601
            remote_addr
            remote_user
            request
            request_method
            scheme
            host
            http_host
            uri
            request_uri
            args
            status
            request_length
            content_length
            bytes_sent
            body_bytes_sent
            upstream_connect_time
            upstream_header_time
            upstream_response_time
            request_time
            http_referer
            http_user_agent
            content_type
            hostname
            pid
    """.strip().split()

    def field_json_item(field):
        try:
            log_field_name, field_content_variable = field.split('=', 1)
        except ValueError:
            log_field_name, field_content_variable = field, field
        return (log_field_name, f'${field_content_variable}')

    return json.dumps(
        {k: v for k, v in map(field_json_item, fields)},
        separators=(',', ':'),  # compact JSON output
    )

with open(sys.argv[1]) as stream:
    template = Template(stream.read())
    print(template.render(log_format_json=log_format_json()), end='')
