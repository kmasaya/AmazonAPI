#!/usr/bin/python3

import json
from bottle import get, run, response

from urls import URLS
from settings import DEBUG

from libs import Amazon


def render_json(raw_dict):
    response.content_type = 'application/json'
    return json.dumps(raw_dict)


@get(URLS['search'])
@get(URLS['search_max'])
@get(URLS['search_index'])
def search_view(keyword, max_count=30, search_index='All'):
    items = Amazon.search(keyword, max_count, search_index)

    return render_json(items)


@get(URLS['asin'])
def asin_view(asin):
    item = Amazon.lookup(asin)

    return render_json(item)


if __name__ == '__main__':
    if DEBUG:
        run(host='localhost', port=8080, reloader=True, debug=True)
    else:
        run(server='cgi')
