from functools import wraps


def debugme(f, kind):

    @wraps(f)
    def wrapped(obj, *args, **kw):

        if kind == "export":
            rows = kw.get("rows", args[0])
            obj.debug_export(rows)

        rv = f(obj, *args, **kw)

        if kind == "import":
            obj.debug_import(rv)

        return rv

    return wrapped



def connectme(f):

    @wraps(f)
    def wrapped(obj, *args, **kw):
        obj.connect()
        rv = f(*args, **kw)
        obj.close()
        return rv

    return wrapped
