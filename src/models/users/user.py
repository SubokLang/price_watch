import uuid
from src.common.database import Database
import src.models.users.errors as UserErrors
from src.common.utils import Utils

class User():
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self.id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that email/password combo as sent by form is valid.
        Checks that e-mail exists and that password is correct
        :param email:
        :param password: A sha512 hashed password
        :return:
        """
        user_data = Database.find_one("users",{"email":email})
        if user_data is None:
            # Tell the user that they don't exist
            raise UserErrors.UserNotExistsError("User not found")
        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell user wrong password
            raise UserErrors.IncorrectPasswordError("Incorrect password")

        return True

    @staticmethod
    def register_user(email, password):
        """
        Registers a user using email and password
        password is hashed as sha-512
        :param email:
        :param password:
        :return:
        """
        user_data = Database.find_one("users", {"email": email})

        if user_data is not None:
            # tell user they are already registered
            pass
        if not Utils.email_is_valid(email):
            # email not constructed properly
            pass

        User(email, Utils.hash_password(password))save_to_db()

        return True

    def save_to_db(self):
        Database.insert("users", self.json)

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }