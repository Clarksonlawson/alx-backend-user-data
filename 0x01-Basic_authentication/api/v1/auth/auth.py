#!/usr/bin/env python3
"""
Module to define the Auth class for authentication.
"""

from flask import request
from typing import List, TypeVar

class Auth:
    """ Template for all authentication systems """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if a path requires authentication """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        return not any([path.startswith(excluded) for excluded in excluded_paths])

    def authorization_header(self, request=None) -> str:
        """ Returns the authorization header """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user """
        return None
