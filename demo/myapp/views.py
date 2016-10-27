from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator


# Create your views here.


def home(request):
	return render(request, 'index.html', {})




# from django.conf.urls import (handler400, handler403, handler404, handler500)
# from django.template import RequestContext
# from django.shortcuts import render, render_to_response

# #point handlers to your view
# handler400 = 'core.views.bad_request'
# handler403 = 'core.views.permission_denied'
# handler404 = 'core.views.page_not_found'
# handler500 = 'core.views.server_error'


# #view example

# # HTTP Error 500
# def server_error(request):
#     response = render_to_response(
#         '500.html',
#         context_instance=RequestContext(request)
#     )
    
#     response.status_code = 500
    
#     return response

# # HTTP Error 404
# def page_not_found(request):
#     response = render_to_response(
#         '404.html',
#         context_instance=RequestContext(request)
#     )
    
#     response.status_code = 404
    
#     return response


