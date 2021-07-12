from threading                              import Thread

from django.conf                            import settings
from django.http                            import HttpResponseForbidden, HttpResponseNotFound

from zigida.common                          import process  as common_process
from zigida.common                          import track    as track_process
from zigida.common                          import visitor  as visitor_process


platform            = settings.PLATFORM
IS_ENV              = settings.IS_ENV
ALLOWED_COUNTRIES   = settings.ALLOWED_COUNTRIES


class FilterCountryMiddleware(object):

    # One-time configuration and initialization.
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        app_type = 'WEB'
        if 'api/' in request.path:
            app_type = 'API'

        lang = 'FR'
        if 'en/' in request.path:
            lang = 'EN'


        i = {
            'app_type'  : app_type,
            'lang'      : lang,
            'page_link' : request.path
        }

        META_INFO = request.META

        if platform == 'linux' and IS_ENV == 'PROD':
            remote_ip = META_INFO.get('HTTP_X_REAL_IP')
            pre_host  = 'https'

        else:
            remote_ip = META_INFO.get('REMOTE_ADDR')
            # TODO
            # TEST TRACKING IP BELOW - TO BE REMOVED IN PRODUCTION
            pre_host = 'http'

        if not remote_ip or remote_ip == '127.0.0.1':
            remote_ip = '185.253.162.139'      # CD
            # remote_ip = '66.249.73.161'     # US
            # remote_ip = '80.82.77.192'      # NL
            # remote_ip = '52.30.16.188'      # IE
            # remote_ip = '13.209.28.104'     # KR
            # remote_ip = '60.217.75.69'      # CN
            # remote_ip = '45.146.165.123'    # RU
            # remote_ip = '37.120.152.100'    # BG

        ip_data = track_process.get_user_ip_data(remote_ip)

        ip_data['pre_host'] = pre_host

        Thread(target=visitor_process.create_visitor, args=(i, request, ip_data)).start()

        found = common_process.exec_binary_search(ALLOWED_COUNTRIES, ip_data.get('country'))

        if not found:
            return HttpResponseNotFound()  # If user's country is not allowed raise Error

        request.META['ip_data'] = ip_data

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
