from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = 'Profile not Found'


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "Can't edit profile you are not author of"