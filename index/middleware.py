from ipware import get_client_ip
from .models import UserData


def get_ip(get_content):

    def middleware(request):
        
        ip, is_routable = get_client_ip(request)
        response = get_content(request)

        all_ips = UserData.objects.values_list('ip')

        if (ip,) in all_ips:
            return response
        
        u = UserData.objects.create(ip=ip, is_routable=is_routable)
        u.save()

        return response

    return middleware