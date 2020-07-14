from django.shortcuts import render
from django.http import HttpResponse
from app.models import Images
from app.serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
# class Medai_Veiw(APIView):
#     def post(self,request,format=None):
#         try:
#             if request.method=='POST':
#                 name=request.POST['name']
#                 location=request.POST['Ilocation']
#                 image=request.POST['image']
#                 d[name]=name.data
#                 d[location]=location.data
#                 d[image]=image.data
#                 return Response(data=d,status=200)
#         except Exception as e:
#              return Response(d.error,status=400)
        

        #         ser=ImageSerializer(data=request.data)
        #         if ser.is_valid():
        #             ser.save()
        #             return Response(data='',status=200)
        # except Exception as e:
        #      return Response(ser.error,status=400)
from app.forms import ImageForm
def image_veiw(request):
    form = ImageForm()
    if request.method=='POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    return render(request,'test.html',{'form':form})

def image_get(request):
    images=Images.objects.all()
    my_dict={'images':images}
    return render(request,'image.html',my_dict)