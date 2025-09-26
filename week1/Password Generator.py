import secrets
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    """
    Generate a strong random password.

    :param length: Length of the password (default: 12)
    :param use_digits: Include digits (0-9) in password
    :param use_symbols: Include symbols (!@#$% etc.) in password
    :return: Generated password string
    """
    alphabet = string.ascii_letters  # A-Z, a-z

    if use_digits:
        alphabet += string.digits     # 0-9
    if use_symbols:
        alphabet += string.punctuation  # !@#$%^&*()_+-=[]{}|;:,.<>?

    if not alphabet:
        raise ValueError("No character sets selected for password generation!")

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


if __name__ == "__main__":
    # Example usage
    print("Generated password:", generate_password(16, use_digits=True, use_symbols=True))

