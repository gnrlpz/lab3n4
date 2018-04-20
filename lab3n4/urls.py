# """lab3n4 URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# from ecommerce import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('admin/', admin.site.urls),
# ]

# from django.conf.urls import url, include
# from rest_framework import routers
# from ecommerce import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserList)
# router.register(r'products', views.ProductList)
# router.register(r'carts', views.CartList)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ecommerce import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^carts/$', views.CartList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^cart/(?P<pk>[0-9]+)/$', views.CartDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)