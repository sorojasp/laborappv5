from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

class ArchivoDemandaView(APIView):

    def get(self,  request, *args, **kwargs):


        files = request.FILES.getlist('demanda')
        files[0]
        print(files)

        path = default_storage.save('tmp/demanda.pdf', ContentFile(files[0].read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        return Response({
                        "hi":"hello"
        }, status=200)
