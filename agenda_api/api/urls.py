from django.urls import include, path
from rest_framework import routers
from . import viewsets
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r"Contats", viewsets.ContactsViewSet)
router.register(r"users", viewsets.UserViewSet, basename="user")





urlpatterns = [ path("", include(router.urls)), 
                path("token/",TokenBlacklistView.as_view(), name="token_obtain_pair"),
                path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
] 