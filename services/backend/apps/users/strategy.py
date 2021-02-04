from rest_framework_jwt.compat import set_cookie_with_token
from rest_framework_jwt.settings import api_settings
from social_django.strategy import DjangoStrategy


class DjangoJWTStrategy(DjangoStrategy):
    def __init__(self, storage, request=None, tpl=None):
        self.token = None
        super(DjangoJWTStrategy, self).__init__(storage, request, tpl)

    def redirect(self, url):
        """
        This method is called multiple times by social_django in various situations.
        One of such cases is when the OAuth2 flow is complete and we redirect user
        back to the web app. In such case an HTTPOnly cookie should be set to a
        JWT created during this step.
        """
        response = super(DjangoJWTStrategy, self).redirect(url)

        if self.token:
            # The token has a defined value, which means this is the
            # last step of the OAuth flow – we can flush the session
            self.session.flush()

            set_cookie_with_token(response, api_settings.JWT_AUTH_COOKIE, self.token)

        return response

    def set_jwt(self, token):
        self.token = token
