from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path,include
from ..api.views import BookList
from django.contrib import admin

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]