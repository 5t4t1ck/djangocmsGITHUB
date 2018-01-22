from extra.models import *

def projects(request):
    u = request.user
    w = Messagerie.objects.filter(receiver = u.username)
    x = w.filter(read = False)
    y = x.count()
    return {'message': y}
