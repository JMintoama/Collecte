from functools import wraps
from django.shortcuts import redirect

def admin_required(destination_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.session.get('admin_logged_in') and request.session.get('destination') == destination_name:
                return view_func(request, *args, **kwargs)
            return redirect(f'/collecte/{destination_name.lower()}/login/')
        return _wrapped_view
    return decorator
