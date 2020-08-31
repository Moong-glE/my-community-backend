from datetime import datetime
from calendar import timegm
from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user):
    """
    Custom JWT payload handler
    Token encrypts the dictionary returned by this function,
        and can be decoded by rest_framework_jwt.utils.jwt_decode_handler
    """
    return {
        'user_id': user.pk,
        'student_id': user.student_id,
        'email': user.email,
        'is_active': user.is_active,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
        'origin_iat': timegm(datetime.utcnow().utctimetuple()),
    }


def jwt_response_payload_handler(token, user):
    """
    Custom JWT response payload handler
    This function controls the custom payload after login or token refresh.
    This data is returned through the web API
    """
    return {
        'token': token,
        'user': {
            'student_id': user.student_id,
            'email': user.email,
        },
    }
