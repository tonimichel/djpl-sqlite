


def refine_DATABASES(original):
    from django_productline.context import PRODUCT_CONTEXT
    return original.update({
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', 
            'NAME': '%s/db.sqlite' % PRODUCT_CONTEXT.PRODUCT_DIR
        }
    })


