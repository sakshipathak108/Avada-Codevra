from django.shortcuts import render
from afterlogin.models import findform, friendlist
from beforereg.models import register_table
from django.contrib.auth.models import User
from django.http import  HttpResponseRedirect


def contact(request):
    return render(request, 'afterlogin/contactus.html')

def faq(request):
    return render(request, 'afterlogin/faq.html')

def join(request):
    if request.method == 'POST':
        joindrop = request.POST['eventjoin']
        dropprof = findform.objects.filter(eventchosen=joindrop)
        return render(request, 'afterlogin/join.html', {'accdrop': dropprof})
    else:
        return render(request, 'afterlogin/join.html')


def profile(request, iidd):
    u = findform.objects.get(pk=iidd)
    dum = u.msid_event
    y = User.objects.get(email=dum)
    x = register_table.objects.get(user=y)
    context = {'alldetails': u, "dets": x}
    return render(request, 'afterlogin/newprof.html', context)


def find(request):
    if request.method == 'POST':
        # fnameevent = request.POST['funame']
        regno = request.POST['reg_no']
        # msidevent = request.POST['msid']
        dropdown = request.POST['eventdrop']
        branchd = request.POST['branch']

        rskills = request.POST['skills']
        yourskills = request.POST['skill']

        findtable = findform(rqd_skills=rskills, eventchosen=dropdown, fname_event=request.user.first_name, regno=regno,
                             your_skills=yourskills,
                             msid_event=request.user.email,branch=branchd)
        findtable.save()
        return HttpResponseRedirect("/loggedin/dashboard/events/")
    else:
        branchd = register_table.objects.get(user=request.user)
        return render(request, 'afterlogin/findnew.html',{"b":branchd})


senderr = None
userrrx = None
userrrx = None
ussery = None


def addteammate(request, iidd):
    senderr = User.objects.get(id=request.user.id)
    dum = senderr.first_name
    usssery = friendlist.objects.get(user__first_name=dum)
    recieverr = findform.objects.get(id=iidd)
    userrrxx = User.objects.get(email=recieverr.msid_event)
    userrrx = friendlist.objects.get(user__email=recieverr.msid_event)
    # usssery.friends.add(userrrxx)
    userrrx.friends.add(senderr)
    return render(request, "afterlogin/newdash.html",
                  {'alert': 'alert to {} was sent succesfully '.format(userrrxx.first_name)}
                  )


def interested(request):
    userfriends = friendlist.objects.get(user=request.user)

    return render(request, "afterlogin/interested.html", {"fr": userfriends})


def events(request):
    x = findform.objects.filter(msid_event=request.user.email)
    return render(request, "afterlogin/events.html", {"de": x})


def deletetheform(request, idev):
    x = findform.objects.filter(id=idev)
    x.delete()
    return HttpResponseRedirect("/loggedin/dashboard/events/")


def search(request):
    query = request.GET['rq_skills']

    searchskills = findform.objects.filter(rqd_skills__icontains=query)
    return render(request, "afterlogin/tp.html", {"ss": searchskills})


def searchbybranch(request):
    query2 = request.GET['branchh']
    searchbranch = findform.objects.filter(branch__icontains=query2)


    return render(request, "afterlogin/searchbybranch.html", {"sb": searchbranch})

