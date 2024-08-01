import globalvariables as gv

def get_all(object):
    return object.objects.all()

def get_all_with_username(object):
    return object.objects.filter(CreatedBy__exact=gv.current_user)

