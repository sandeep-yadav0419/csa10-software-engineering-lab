"""Small login function for the feature-login branching exercise.

Provide a generated password hash explicitly; no production credentials live here.
This function is not a complete authentication server.
"""
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password, users):
    stored=users.get(username)
    if stored and check_password_hash(stored,password):
        return 'Login Successful'
    return 'Invalid Credentials'

if __name__=='__main__':
    from getpass import getpass
    demo_password=getpass('Set a temporary lab password: ')
    if not demo_password:
        raise SystemExit('Password cannot be empty.')
    demo_users={'admin':generate_password_hash(demo_password)}
    print(login(input('Username: '),getpass('Password: '),demo_users))
