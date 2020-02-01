from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import os

from .clone import REsearch


def index(request):
    return render(request, 'index.html')


def upload(request):

    if request.method == 'POST':

        fields = request.POST

        mcs, goi = fields.get('mcs'), fields.get('goi')

        print(f'{mcs} and {goi}')

        files = request.FILES
        mcsFile, goiFile = files.get('mcsFile'), files.get('goiFile')
        fs = FileSystemStorage()
        if mcsFile:
            name = fs.save(mcsFile.name, mcsFile)
            mcsFile = os.path.join(fs.location, name)
        if goiFile:
            name = fs.save(goiFile.name, goiFile)
            goiFile = os.path.join(fs.location, name)

        REs = REsearch(goi, goiFile, mcs, mcsFile)

        # if not f.name.rsplit('.')[1] in ['dna', 'fasta']:
        # message.error(request, 'File type not supported.')

        REs = [f'{str(e):<10s} { "blunt" if e.is_blunt() else e.elucidate()}' for e in REs]

        return render(request, 'result.html', {'REs': REs})

    else:
        return render(request, 'upload.html')


def result(request):
    return HttpResponse('sex')
