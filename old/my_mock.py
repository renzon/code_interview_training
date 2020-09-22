from functools import wraps


def method3(x: int, y: int) -> str:
    """
    Typical
    Usage:

    method3(1, 4)
    method3(9, 2)
    """
    z = method4(x, y)
    a = method5(z)
    b = method6(a, x, y)
    return b


def test_method3():
    ret = method3(1, 2)

    assert method4.args == (1, 2)
    assert method5.args == (method4.ret,)
    assert method6.args == (method5.ret, 1, 2)
    assert method6.ret == ret


def my_mock(fcn):
    @wraps(fcn)
    def decorator(*args, **kwargs):
        decorator.args = args  # store args
        decorator.ret = fcn(*args, **kwargs)  # store fcn return
        return decorator.ret

    return decorator


@my_mock
def method4(x, y):
    return 4


@my_mock
def method5(z):
    return 5


@my_mock
def method6(a, x, y):
    return 6
