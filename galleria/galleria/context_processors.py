from django.conf import settings

def galleria_context_processor(request):
    my_dict = {
        'galleria_brand': settings.GALLERIA_BRAND,
        'galleria_frontpage': settings.GALLERIA_FRONTPAGE,
    }

    return my_dict
