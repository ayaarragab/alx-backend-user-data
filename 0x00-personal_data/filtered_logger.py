#!/usr/bin/env python3
"""
a function called filter_datum that returns
the log message obfuscated:

Arguments:
=> fields: a list of strings representing all
fields to obfuscate
=> redaction: a string representing by what
the field will be obfuscated
=> message: a string representing the log line
=> separator: a string representing all fields in the
log line (message)
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(
            self.fields,
            RedactingFormatter.REDACTION,
            record.getMessage(),
            RedactingFormatter.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Replaces occurrences of the specified fields in the
    message with the redaction string.

    :param fields: List of fields to redact in the message.
    :param redaction: The string to replace field values with.
    :param message: The original log message.
    :param separator: The separator used in the log message.
    :return: The log message with the specified fields redacted.
    """
    for field in fields:
        pattern = rf"{field}=[^{separator}]*"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message
