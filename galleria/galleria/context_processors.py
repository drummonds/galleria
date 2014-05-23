from django.conf import settings

def galleria_context_processor(request):
    my_dict = {
        'galleria_brand': settings.GALLERIA_BRAND,
    }

    return my_dict
