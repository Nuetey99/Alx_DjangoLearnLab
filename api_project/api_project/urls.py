
from django.urls import path,include
from ..api.views import BookList
from django.contrib import admin

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]