from django.shortcuts import render
from afterlogin.models import findform
from beforereg.models import register_table
from django.contrib.auth.models import User
def contact(request):
    return render(request, 'afterlogin/contactus.html')


def join(request):
    if request.method == 'POST':
        joindrop = request.POST['eventjoin']
        dropprof = findform.objects.filter(eventchosen=joindrop)
        return render(request, 'afterlogin/join.html',{'accdrop': dropprof})
    else:
        return render(request, 'afterlogin/join.html')


def profile(request, iidd):
        u = findform.objects.get(pk = iidd)
        return render(request, 'afterlogin/profile.html', {'alldetails':u})


def find(request):
    if request.method == 'POST':
        fnameevent = request.POST['funame']
        lnameevent = request.POST['lname']
        msidevent = request.POST['msid']
        dropdown = request.POST['eventdrop']
        rskills = request.POST['skills']

        findtable = findform(rqd_skills=rskills, eventchosen=dropdown,fname_event=fnameevent, lname_event=lnameevent,
                             msid_event=msidevent)
        findtable.save()
        return render(request, 'afterlogin/join.html')
    else:
        return render(request, 'afterlogin/findnew.html')
