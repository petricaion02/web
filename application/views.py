from django.shortcuts import render

def get_token_view(request):
    return render(request=request, template_name='js_login.html')
