from django.urls                                        import path, include

from zigida.apps.web.products.products.list.views       import ProductMenListView
from zigida.apps.web.products.products.list.views       import ProductWomenListView


app_name = 'main_products'

urlpatterns = [

    path('mens/',                   ProductMenListView.as_view(),               name='mens'),
    path('womens/',                 ProductWomenListView.as_view(),             name='womens'),

    # path('categories/',             include('zigida.apps.web.products.categories.urls')),
    # path('colors/',                 include('zigida.apps.web.products.colors.urls')),
    path('products/',               include('zigida.apps.web.products.products.urls')),
    # path('sizes/',                  include('zigida.apps.web.products.sizes.urls')),

]
