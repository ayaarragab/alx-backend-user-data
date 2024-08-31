#!/usr/bin/env python3
"""
a hash_password function that expects one
    string argument name password and returns
    a salted, hashed password, which is a byte string
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns byte string password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    is_valid function that expects 2 arguments and returns a boolean.

    Arguments:

    hashed_password: bytes type
    password: string type
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
