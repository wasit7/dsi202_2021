from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    print()
    message="id:%s, uasername:%s firstname:%s, lastname:%s"%(request.user.pk, request.user.username, request.user.first_name, request.user.last_name)
    now = datetime.datetime.now()
    html = "<html><body><p>It is now %s.</p><p>%s</p></body></html>" % (now,message)
    return HttpResponse(html)