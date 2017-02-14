from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage


#@login_required
def Add(request):
    if request.method == 'POST' and request.FILES['project']:
        project = request.FILES['project']
        fs = FileSystemStorage()
        filename = fs.save(project.name, project)
        uploaded_file_url = fs.url(filename)
        return render(request, 'addproject/index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'addproject/index.html')

