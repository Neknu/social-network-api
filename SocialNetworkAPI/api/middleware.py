import jwt
import traceback

from django.utils import timezone
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.middleware import get_user

from .models import Profile


class UpdateLastActivityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'), 'Requires authentication middleware'
        user = self.get_jwt_user(request)
        if user.is_authenticated:
            Profile.objects.filter(user__id=user.id) \
                           .update(last_activity=timezone.now())

    @staticmethod
    def get_jwt_user(request):

        user_jwt = get_user(request)
        if user_jwt.is_authenticated:
            return user_jwt

        if 'Authorization' not in request.headers:
            return AnonymousUser()

        # remove 'Bearer ' from token
        token = request.headers['Authorization'][7:]
        user_jwt = AnonymousUser()
        if token is not None:
            try:
                user_jwt = jwt.decode(token, None, None)
                user_jwt = User.objects.get(
                    id=user_jwt['user_id']
                )
            except Exception as e:  # NoQA
                traceback.print_exc()
        return user_jwt
