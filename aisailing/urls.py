from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from article import views


from rest_framework.routers import DefaultRouter
from article import views
router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'tag', views.TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/article/', include('article.urls', namespace='article')),
    # drf 自动注册路由
    path('api/', include(router.urls)),

]