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
        if not Utils.check_hashed_password(password, user_data['password'])
            # Tell user wrong password
            raise UserErrors.IncorrectPasswordError("Incorrect password")

        return True