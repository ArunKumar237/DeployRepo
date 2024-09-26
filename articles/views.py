# views.py
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Send email after successfully creating the article
        article_title = serializer.data.get('title')
        article_content = serializer.data.get('content')
        
        # Replace these values with the actual email configuration
        recipient_email = 'recipient@example.com'  # Email of the recipient
        subject = f"New Article Created: {article_title}"
        message = f"Title: {article_title}\n\nContent:\n{article_content}"
        from_email = 'your_email@example.com'  # Your email address

        # Send the email
        send_mail(
            subject,
            message,
            from_email,
            [recipient_email],  # List of recipient emails
            fail_silently=False,
        )

        # Return a success response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

