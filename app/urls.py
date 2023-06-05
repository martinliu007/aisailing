from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
]