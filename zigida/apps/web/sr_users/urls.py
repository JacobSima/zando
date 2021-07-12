from django.urls                                    import path, include

from zigida.apps.web.home.views                     import ZigHomeView
from zigida.apps.web.sr_users.views import UserLoginView

app_name = 'web'

urlpatterns = [

        path('login/',                        UserLoginView.as_view(),                  name='home'),
        # path('about/',                  ZigAboutView.as_view(),                 name='about'),
        # path('contact/',                ZigContactView.as_view(),               name='contact'),
        # path('mens/',                   ZigMensView.as_view(),                  name='mens'),
        # path('womens/',                 ZigWomensView.as_view(),                name='womens'),

        # path('customers/',            include('zigida.apps.web.customers.urls')),
        # path('orders/',               include('zigida.apps.web.orders.urls')),
        # path('products/',             include('zigida.apps.web.products.urls')),

    ]
