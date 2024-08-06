#!/usr/bin/env python3
"""
Base authentication module.
"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        for p in excluded_paths:
            if p.endswith('*'):
                if path.startswith(p[:-1]):
                    return False
            else:
                if path == p:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        return None
