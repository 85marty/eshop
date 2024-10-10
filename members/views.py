from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm


def members_old(request):
    return HttpResponse("Hello world!")


def members_old_two(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def members(request):
    return render(request, 'index.html')


def all_members(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request, 'all_members.html', context)


def detail(request, id):
    member = Member.objects.get(id=id)
    context = {
        'member': member,
    }
    return render(request, 'detail.html', context)


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['firstname']
            last_name = form.cleaned_data['lastname']
            greeting = f"Hi, {first_name} {last_name}"
            form.save()
            return redirect('all_members')

    return render(request, 'add_member.html', {'form': MemberForm()})
