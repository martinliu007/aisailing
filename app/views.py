from app.models import App
from app.permissions import IsAdminUserOrReadOnly
from rest_framework import viewsets
from app.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)