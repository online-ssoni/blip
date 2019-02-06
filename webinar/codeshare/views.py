from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('download')
    else:
        form = DocumentForm()
    return render(request, 'codeshare/index.html', {
        'form': form
    })


# def download(request):
#     q = Document.objects.all()
#     x = []
#     for que in q:
#         s = que.document.url
#         url = s.split('/')
#         del url[0]
#         x.append("/".join(url)) 
#     return render(request, 'codeshare/download.html', {'q':x})
