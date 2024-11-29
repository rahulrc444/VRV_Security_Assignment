from django.shortcuts import redirect

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin_dashboard/') and request.user.role != 'admin':
            return redirect('login')
        if request.path.startswith('/moderator_dashboard/') and request.user.role != 'moderator':
            return redirect('login')
        if request.path.startswith('/user_dashboard/') and request.user.role != 'user':
            return redirect('login')
        return self.get_response(request)
