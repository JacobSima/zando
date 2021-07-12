from django.urls                                            import path

from zigida.apps.web.products.products.create.views         import ProductCreateView
# from zigida.apps.web.products.products.delete.views         import ProductDeleteView
from zigida.apps.web.products.products.list.views           import ProductMenListView
from zigida.apps.web.products.products.list.views           import ProductWomenListView
# from zigida.apps.web.products.products.update.views         import ProductUpdateView


app_name = 'products'

urlpatterns = [

    # path('mens/',                   ProductMenListView.as_view(),               name='mens'),
    # path('womens/',                 ProductWomenListView.as_view(),             name='womens'),

    path('create/',                 ProductCreateView.as_view(),                name='create'),
    # path('delete/<code>',           ProductDeleteteView.as_view(),              name='delete'),
    # path('list/',                   ProductListView.as_view(),                  name='list'),
    # path('update/<code>',           ProductUpdateView.as_view(),                name='update'),

]
