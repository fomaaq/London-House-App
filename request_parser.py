from fastapi import Request
from urllib.parse import parse_qs
from collections import defaultdict


def get_parameters(request: Request) -> dict:
    request_parameters = parse_qs(request.url.query, keep_blank_values=True)
    result_dict = dict((k, v if len(v) > 1 else v[0]) for k, v in request_parameters.items())
    return defaultdict(lambda: None, result_dict)
