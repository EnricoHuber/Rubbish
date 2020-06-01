import string


def password_validator(password):
    flag_num = False
    flag_spec_char = False
    """ First check is the length """
    if len(password) < 5:
        return False
    elif len(password) > 10:
        return False
    else:
        """ Now check for the single character """
        for char in password:
            if char in string.whitespace:           # Avoid spaces
                return False
            elif char in string.digits:             # Should contain at least a number
                flag_num = True
            elif char in string.punctuation:        # Should contain at least a special character
                flag_spec_char = True
    if flag_num and flag_spec_char:
        return True
    else:
        return False


def main():
    password_in = input("Insert the password: ")
    print(password_validator(password_in))


if __name__ == '__main__':
    main()
