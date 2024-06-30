from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from yadja.forms import PhotoForm
from yadja.models import Photo


# Create your views here.
def index_view(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            print('form valid', form.cleaned_data['image'].image)
            p = Photo(image=form.cleaned_data['image'], name=form.cleaned_data['name'])
            p.save()
            return HttpResponseRedirect("/")
    else:
        form = PhotoForm()
    template_name = "yadja/index.html"
    qs = Photo.objects.order_by('-id')[:10]
    context = {
        "photos": qs,
        "form": form,
    }
    return render(request, template_name=template_name, context=context)

