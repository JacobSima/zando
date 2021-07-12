from django.urls                                                import path, include

from zigida.apps.web.home.views                                 import HomeView
from zigida.apps.web.home.views                                 import AboutView, Zig404View
from zigida.apps.web.sr_users.views                             import UserLoginView, \
                                                                        UserRegisterView, UserLogoutView
# from zigida.apps.web.products.list.views                        import ZigMensView
# from zigida.apps.web.products.list.views                        import ZigWomensView

# from zigida.apps.web.accounting.addresses.urls                  import urlpatterns as addresses_urls
# from zigida.apps.web.accounting.banks.urls                      import urlpatterns as banks_urls
# from zigida.apps.web.accounting.coupons.urls                    import urlpatterns as coupons_urls
# from zigida.apps.web.accounting.items.urls                      import urlpatterns as items_urls
# from zigida.apps.web.accounting.orders.urls                     import urlpatterns as orders_urls
# from zigida.apps.web.accounting.payments.urls                   import urlpatterns as payments_urls
# from zigida.apps.web.accounting.receipts.urls                   import urlpatterns as receipts_urls
# from zigida.apps.web.accounting.refunds.urls                    import urlpatterns as refunds_urls
# from zigida.apps.web.accounting.vouchers.urls                   import urlpatterns as vouchers_urls

# from zigida.apps.web.categories.urls                            import urlpatterns as categories_urls
# from zigida.apps.web.customers.urls                             import urlpatterns as customers_urls
# from zigida.apps.web.dashboard.urls                             import urlpatterns as dashboard_urls
# from zigida.apps.web.openinghours.urls                          import urlpatterns as openinghours_urls
from zigida.apps.web.products.urls                              import urlpatterns as products_urls
# from zigida.apps.web.sr_issues.urls                             import urlpatterns as sr_issues_urls
# from zigida.apps.web.sr_users.urls                              import urlpatterns as sr_users_urls
# from zigida.apps.web.stores.urls                                import urlpatterns as stores_urls


app_name = 'web'

urlpatterns = [

        path('',                            HomeView.as_view(),                     name='home'),
        path('about/',                      AboutView.as_view(),                    name='about'),
        # path('contact/',                  ZigContactView.as_view(),               name='contact'),
        # path('mens/',                     ZigMensView.as_view(),                  name='mens'),
        # path('womens/',                   ZigWomensView.as_view(),                name='womens'),
        path('404/',                        Zig404View.as_view(),                   name='404'),

        path('login/',                      UserLoginView.as_view(),                name='login'),
        path('logout/',                     UserLogoutView.as_view(),               name='logout'),
        path('register/',                   UserRegisterView.as_view(),             name='register'),

        # path('customers/',                include('zigida.apps.web.customers.urls')),
        path('issues/',                     include('zigida.apps.web.sr_issues.urls')),
        # path('orders/',                   include('zigida.apps.web.orders.urls')),
        # path('products/',                   include('zigida.apps.web.products.urls')),

    ] + products_urls
