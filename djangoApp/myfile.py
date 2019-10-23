# -*- coding: utf-8 -*-

from django.http import HttpResponse
import os
import sys  

reload(sys)
sys.setdefaultencoding('utf8')

def upload_file(request):
    if request.method == 'POST':
        print request.FILES
        obj = request.FILES.get('files')
        f = open(os.path.join('upload',obj.name),'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()
        return HttpResponse('{"msg":"上传成功"}')
    else:
        return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)