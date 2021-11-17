from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def uploadview(request):
    context = {}
    if request.method == 'POST':
        uplaoded_file = request.FILES['dcmt']
        fs = FileSystemStorage()
        name = fs.save(uplaoded_file.name, uplaoded_file)
        context['url'] = fs.url(name)
    return render(request, 'mediaapp/home.html', context)
