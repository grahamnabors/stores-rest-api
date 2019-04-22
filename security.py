from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username) # Previously this line was 'user = username_mapping.get(username, None)' when using commented out code above.
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id) # Previously was 'return userid_mapping.get(user_id, None)' when using commented out code above.