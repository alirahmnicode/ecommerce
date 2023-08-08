from django.db import connection, reset_queries


def query_manage(fn):
    def inner(*args, **kwargs):
        reset_queries()
        result = fn(*args, **kwargs)
        queries_ = connection.queries
        print("*" * 100)
        print("{0} view called with {1} queries".format(fn.__name__, len(queries_)))
        print("\n" + "\n--------------\n".join(f"{v['sql']}" for v in queries_))
        print("*" * 100)
        return result

    return inner
