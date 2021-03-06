#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Copyright (C) 2014:
#    Gabes Jean, naparuba@gmail.com


import json
import base64

# try pygments for pretty printing if available
try:
    import pygments
    import pygments.lexers
    import pygments.formatters
except ImportError:
    pygments = None

from kunai.log import cprint, logger
from kunai.unixclient import get_json, get_local, request_errors
from kunai.cli import get_kunai_json, get_kunai_local, print_info_title, print_2tab, post_kunai_json


def do_evaluator_list():
    try:
        (code, r) = get_kunai_local('/agent/evaluator/list')
    except request_errors, exp:
        logger.error(exp)
        return

    try:
        d = json.loads(r)
    except ValueError, exp:  # bad json
        logger.error('Bad return from the server %s' % exp)
        return

    print_info_title('Functions')
    for fname in d:
        print fname


def do_evaluator_eval(expr):
    print expr
    expr_64 = base64.b64encode(expr)
    try:
        r = post_kunai_json('/agent/evaluator/eval', {'expr':expr_64})
    except request_errors, exp:
        logger.error(exp)
        return

    print_info_title('Result')
    print r


exports = {
    do_evaluator_list: {
        'keywords'   : ['evaluator', 'list'],
        'args'       : [
        ],
        'description': 'List evaluator functions'
    },
    do_evaluator_eval: {
        'keywords'   : ['evaluator', 'eval'],
        'args'       : [
            # {'name' : '--expression', 'description':'Expression to eval'},
        ],
        'description': 'Evaluate an expression'
    },

}
