from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

path('books/', views.book_list,  name='bool_list'),
path('book/create', views.book_create, name='book_create'),
path('book/<int:id>/', views.book_detail, name='book_detail')
]
urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

