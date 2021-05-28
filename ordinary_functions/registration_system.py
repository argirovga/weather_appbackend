from personal_api.models import User_preferences
import secrets


def generate_token() -> str:
    """
    Генерация токена

    :return: уникальный токен пользователя
    """
    user_id = secrets.token_hex(8)
    if user_id in User_preferences.objects.values_list('user_id', flat=True):
        user_id = secrets.token_hex(8)
    return user_id


def check_access(user_id, name) -> bool:
    """
    Проверка на наличие доступа к данным пользователя

    :return: разрешение или отказ в доступе
    """
    templ = User_preferences.objects.filter(user_id=user_id, name=name)
    if len(templ) == 0:
        return False
    if len(templ) > 0:
        return True

