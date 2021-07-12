from django.urls                                        import path

from zigida.apps.web.products.products.list.views       import ProductMenListView
from zigida.apps.web.products.products.list.views       import ProductWomenListView


app_name = 'stores'

urlpatterns = [

    path('mens/',               ProductMenListView.as_view(),               name='mens'),
    path('womens/',             ProductWomenListView.as_view(),             name='womens'),

]
