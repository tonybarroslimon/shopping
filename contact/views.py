from datetime import date

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from .forms import ContactUsForm

def contact(request):
    form = ContactUsForm(request.POST or None)
    if form.is_valid():
        this_form = form.save(commit=False)
        this_form.save()
        return HttpResponseRedirect('/')
    return render_to_response('contact/form.html', locals(), context_instance=RequestContext(request))
