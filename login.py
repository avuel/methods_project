def get_username() -> str:
    try:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        return input('Enter your username: ')

    except Exception:
        return None

def get_password() -> str:
    try:
        return input('Enter your password: ')

    except Exception:
        return None