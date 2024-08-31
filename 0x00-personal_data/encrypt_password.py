#!/usr/bin/env python3
"""
a hash_password function that expects one
    string argument name password and returns
    a salted, hashed password, which is a byte string
"""
from bcrypt import hashpw, gensalt
import hashlib
import base64
from typing import ByteString


def hash_password(password) -> ByteString:
    """
    a hash_password function that expects one
    string argument name password and returns
    a salted, hashed password, which is a byte string
    """
    password = b"an incredibly long password" * 10
    hashed = hashpw(
        base64.b64encode(hashlib.sha256(password).digest()),
        gensalt()
    )
    return hashed
