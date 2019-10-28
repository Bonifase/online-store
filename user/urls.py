from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views
from store import views as store_views

router = DefaultRouter()

router.register('profile', views.UserViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('store', store_views.ProductViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
