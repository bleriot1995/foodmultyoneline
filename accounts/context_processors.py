from django.conf import settings
from accounts.models import UserProfile
from vendor.models import Vendor


def get_vendor(request):
    try:
        vendor = Vendor.objects.get(user=request.user)
    except Exception:
        vendor = None
    return dict(vendor=vendor)


