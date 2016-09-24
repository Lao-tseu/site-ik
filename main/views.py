from django.shortcuts import render, HttpResponse, redirect
from main.models import IK, Article

# Create your views here.
def index(request):
    numeros = IK.objects.all()
    return render(request, 'index.html', {'numeros' : numeros})

def submit(request):
    articles = Article.objects.all()
    return render(request, 'submit.html', {'articles' : articles})

def show(request, id):
    ik = IK.objects.get(id=id)
    response = HttpResponse(ik.fichier, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename="+str(ik.numero)+".pdf"
    return response

#Login temporaire
def login(request, auth):
    request.session['auth'] = auth
    return redirect(index)

def logout(request):
    del request.session["username"]
    request.session.modified = True
    return redirect("/")

#Partie Frankiz
def fkz_answer(request):
    if not "timestamp" in request.GET.keys() or not "response" in request.GET.keys() or not "hash" in request.GET.keys():
        return redirect("/login_required/")
    response = request.GET.get("response")
    ts = request.GET.get("timestamp")
    h = request.GET.get("hash")

    if abs(int(timestamp()) - int(ts)) > 600:
        return redirect("/login_required/")

    if hashlib.md5(ts + FKZ_KEY + response).hexdigest() != h:
        return redirect("/login_required/")

    data = json.loads(response)
    request.session['username'] = data['hruid']
    return redirect("/")

def fkz_do_login(request):
    ts = timestamp()
    page = "http://***/fkz_answer/"
    r = json.dumps(["names", "email"])
    h = hashlib.md5(ts + page + FKZ_KEY + r).hexdigest()
    return redirect("http://www.frankiz.net/remote?"+urlencode([('timestamp',ts),('site',page),('hash',h),('request',r)]))
