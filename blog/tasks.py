# importing the necessary libraries
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa  
from django.core.files.base import ContentFile
from celery import shared_task
from celery.utils.log import get_task_logger

from .models import BlogPost



@shared_task(bind=True)
def create_blog_post_pdf(self, **kwargs):
    instance = BlogPost.objects.get(pk=kwargs["pk"])
    template = get_template('blog/post_pdf.html')
    html  = template.render({'post': instance})
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        instance.pdf = ContentFile(result.getvalue(), f'{("BlogPost_")}_{instance.slug}.pdf')
        instance.pdf_created = True
        instance.save()