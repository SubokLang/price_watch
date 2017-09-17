from passlib.hash import pbkdf2_sha512

class Utils():

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email)else False

    @staticmethod
    def hash_password(password):
        """
        Hashes a pw using pbkdf2_sha512
        :param password:    sha512 from login
        :return:            sha512 -> pbkdf2_sha512
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password from user matches db password
        db pw is more encrypted than entered password
        :param password:            sha-512-hashed pw
        :param hashed_password:     pbkdf2_sha512 encryption
        :return:
        """
        return pbkdf2_sha512.verify(password, hashed_password)