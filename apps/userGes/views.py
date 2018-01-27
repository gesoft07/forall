from django.db import connection
from django.views.generic import TemplateView


# def index2(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


class indexView(TemplateView):
    with connection.cursor() as c:
        c.callproc('toDjango', [1])
        # username = [item[0] for item in c.fetchall()]
        email = [item[1] for item in c.fetchall()]
        print(email)
    template_name = "index.html"
