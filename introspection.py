def introspection_info(obj):
    obj_type = type(obj)
    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    module = obj.__class__.__module__
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }
    return info


number_info = introspection_info(42)
print(number_info)
