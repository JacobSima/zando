from django.urls                                import path, include


urlpatterns = [

        # path('api/',                        include('zigida.apps.api.urls')),
        # path('autocomplete/',               include('zigida.apps.autocomplete.urls')),
        path('',                                include('zigida.apps.web.urls')),

    ]
