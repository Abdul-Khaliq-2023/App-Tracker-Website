from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import UserData

def appPage(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def loginpage(request):
  template = loader.get_template('Website/a_home/templates/registration/login.html')
  return HttpResponse(template.render())

def save_data(request):
    if request.method == 'POST':
        input_data1 = request.POST.get('inputData1')
        input_data2 = request.POST.get('inputData2')
        dropdown_value1 = request.POST.get('dropDown1')
        dropdown_value2 = request.POST.get('dropDown2')
        UserData.objects.create(input_data1=input_data1, input_data2 = input_data2, dropdown_value1 = dropdown_value1, dropdown_value2 = dropdown_value2)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
