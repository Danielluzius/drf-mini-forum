from rest_framework.throttling import UserRateThrottle


class PostThrottle(UserRateThrottle):
    scope = 'posts'
    
    def allow_request(self, request, view):
        # Only POST requests are limited by this throttle
        if request.method != 'POST':
            return True
        
        # For POST requests: apply standard throttling
        return super().allow_request(request, view)
