#!/usr/bin/env python3
from flask import request
from os import getenv

class Auth:
    def session_cookie(self, request=None):
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))
