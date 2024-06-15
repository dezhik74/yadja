from django.shortcuts import render

# Create your views here.
def index_view(request):
    template_name = "yadja/index.html"
    return render(request, template_name=template_name)

