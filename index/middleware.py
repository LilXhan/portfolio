from ipware import get_client_ip
from .models import UserData


def get_ip(get_content):

    def middleware(request):
        
        ip, is_routable = get_client_ip(request)
        response = get_content(request)

        count = 0

        if count == 0:
            u = UserData.objects.create(ip=ip, is_routable=is_routable)
            u.save()
            count += 1
            return response

        all_ips = UserData.objects.values_list('ip')

        if (ip,) not in all_ips:
            u = UserData.objects.create(ip=ip, is_routable=is_routable)
            u.save()
            return response

        return response

    return middleware