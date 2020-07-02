from django.http import HttpResponse , HttpResponseNotFound

def home(request):
    return HttpResponse('hi, from home')
    

def profile(request, username):
    data = {
        'ram': 'Ram Bdr',
        'Hari': 'hari bdr',
        'shyam' : 'Shyam bahadur'
    }

    full_name = data.get(username)

    if not full_name:
        #return HttpResponseNotFound('The username doesnot exit')
        return HttpResponseNotFound('The username doesnot exit', status = 404 ) 
    
    string_data  = f"Your name is:{full_name}"
    return HttpResponse(string_data)
        


        

      
        




