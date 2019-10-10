from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from memberships.views import IdDocumentsViewSet, UserViewSet

# Routers provide an easy way of automatically
# determining the URL conf.
router = routers.DefaultRouter()
router.register(r'id_document', IdDocumentsViewSet, basename='id_document')
router.register(r'users', UserViewSet, basename='user')
router.register(r'members', MemberViewSet, basename='member')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
