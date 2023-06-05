from app.models import App
from app.serializers import ArticleListSerializer
from app.serializers import ArticleDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from app.permissions import IsAdminUserOrReadOnly



# 文章列表
class ArticleList(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = ArticleListSerializer

    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# 文章详情
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]