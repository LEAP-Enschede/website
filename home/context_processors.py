from .models import MenuItem


def menu_processor(request):
    menu = MenuItem.objects.filter(parent__isnull=True)
    return {'menu': menu}
