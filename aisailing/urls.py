from django.contrib import admin
from django.urls import path
from django.urls import include


from rest_framework.routers import DefaultRouter
from app import views
router = DefaultRouter()
router.register(r'app', views.ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/article/', include('app.urls', namespace='app')),
    # drf 自动注册路由
    path('api/', include(router.urls)),
]