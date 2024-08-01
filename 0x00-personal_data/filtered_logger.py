#!/usr/bin/env python3
"""
Module for filtering and logging personal data.
"""

import re
import logging
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Replaces the values of specified fields with the redaction string.
    
    Args:
        fields (List[str]): List of field names to redact.
        redaction (str): The string to replace field values with.
        message (str): The original message containing fields and values.
        separator (str): The character separating fields in the message.
    
    Returns:
        str: The message with specified fields redacted.
    """
    pattern = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)

def get_logger() -> logging.Logger:
    """
    Creates a logger with a StreamHandler and a RedactingFormatter.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger
