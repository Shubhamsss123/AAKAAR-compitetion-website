from django.shortcuts import redirect
def redirect_view1(request):
    response = redirect('cr/')
    return response