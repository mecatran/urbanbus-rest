# -*- coding: utf-8 -*-

from flask import jsonify
from utils.timer import get_time
from utils.logger import log_performance

def call_service(functionToRun, responseType, **kwargs):
    start = get_time()
    response = ""
    try:
        response = jsonify({ responseType: functionToRun(**kwargs) })
    except Exception as e:
        response = error(str(e))
    finally:
        end = get_time()
        params = "| GET endpoint = /"+responseType+" | "+str(kwargs)
        log_performance(start, end, params, "performance.log")
        return response
