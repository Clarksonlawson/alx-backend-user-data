#!/usr/bin/env python3
"""
Module for password hashing and validation.
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a given password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain text password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
