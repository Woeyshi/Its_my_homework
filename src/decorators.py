import traceback
from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional, Union


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, логирующий вызов функции и ее результат.
    """

    def decorator(func: Callable) -> Callable:
        """
        Внутренняя функция декоратора, которая обертывает декорируемую функцию.
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Union[str, Any]:
            """
            Выполняет логирование до и после вызова декорируемой функции.
            """
            try:
                result = func(*args, **kwargs)
                log_message = f"{datetime.now()}: {func.__name__} ok\n"
            except Exception as e:
                result = None
                log_message = (
                    f"{datetime.now()}: {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                )
                traceback_msg = traceback.format_exc()

            if filename:
                with open(filename, "a") as file:
                    file.write(log_message)
                    if "traceback_msg" in locals():
                        file.write(traceback_msg)
            else:
                print(log_message)
                if "traceback_msg" in locals():
                    print(traceback_msg)

            if isinstance(result, Exception):
                raise result

            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """
    Пример функции, которая складывает два числа.
    """
    return x + y


my_function(1, 2)
