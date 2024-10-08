#!/usr/bin/env python3
"""
a hash_password function that expects one
    string argument name password and returns
    a salted, hashed password, which is a byte string
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from user import User
from uuid import uuid4


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        registering user
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashedpass = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hashedpass)
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """
        validate login
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        creates session_id of a user
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            pass
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(
            self, session_id: str) -> Union[User, None]:
        """
            gets user from session_id
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
            destroys session of a user
        """
        self._db.update_user(user_id, session_id=None)


def _hash_password(password: str) -> bytes:
    """ Returns byte string password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
        The function should return a
        string representation of a new UUID.
    """
    return str(uuid4())
