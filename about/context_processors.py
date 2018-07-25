from .models import GeneralInformation
from blog.models import Blog


def general_information(request):
    information = GeneralInformation.objects.first()
    blog_widget = Blog.objects.all()[:2]
    context = {
        'information': information,
        'blog_widget': blog_widget
    }
    return context
