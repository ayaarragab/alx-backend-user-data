#!/usr/bin/env python3
"""
a hash_password function that expects one
    string argument name password and returns
    a salted, hashed password, which is a byte string
"""
import bcrypt
import hashlib
import base64
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """
    a hash_password function that expects one
    string argument name password and returns
    a salted, hashed password, which is a byte string
    """
    password: str = b"an incredibly long password" * 10
    hashed: ByteString = bcrypt.hashpw(
        base64.b64encode(hashlib.sha256(password).digest()),
        bcrypt.gensalt()
    )
    return hashed
