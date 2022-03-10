from pprint import pprint
from functools import wraps

pprint(globals())

def my_logger(origin_func):
    import logging
    logging.basicConfig(filename=f"{origin_func.__name__}.log", level=logging.INFO)
    @wraps(origin_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args}, and kwargs: {kwargs}"
        )
        return origin_func(*args, **kwargs)

    return wrapper


def my_timer(origin_func):

    import time

    # @wraps(origin_func)
    def wrapper_timer(*args, **kwargs):
        t1 = time.time()
        result = origin_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"Function '{origin_func.__name__}' ran in {t2} seconds")
        return result

    return wrapper_timer


def test_log(func):

    # @wraps(func)
    def wrapper_test_log(*args, **kwargs):
        print(f"Entre dans la fonction {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Sort de la fonction '{func.__name__}' ")
        return result

    return wrapper_test_log


@my_timer
@test_log
def first_kwarg(*args, **kwargs):
    liste = []
    for action in args:
        for clef, valeur in kwargs.items():
            liste.append(f'{action} {clef} {valeur} !!!')
    print(liste)


liste_phrase = first_kwarg("Lol", nom="Chaton")
