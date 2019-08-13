from functools import wraps
from flask import g


def plugin_available():
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            for func in getattr(g, 'call_before_{}'.format(fn.__name__), ()):
                func()
            response = fn(*args, **kwargs)
            for func in getattr(g, 'call_after_{}'.format(fn.__name__), ()):
                response = func(response)
            return response
        return decorated_view
    return wrapper


def plugin(rule, endpoint):
    def decorator(f):
        if rule not in ('before', 'after'):
            raise ValueError('could not find rule {} in {}'.format(
                rule,
                ('before', 'after')
            ))

        if not hasattr(g, 'call_{}_{}'.format(rule, endpoint)):
            g['call_{}_{}'.format(rule, endpoint)] = []
        g['call_{}_{}'.format(rule, endpoint)].append(f)

        return f
    return decorator
