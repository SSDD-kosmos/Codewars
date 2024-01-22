import time


class TimerContextManager:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        execution_time = self.end_time - self.start_time
        print(f"Время выполнения: {execution_time} сек.")


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения: {execution_time} сек.")
        return result
    return wrapper


# Пример использования класса TimerContextManager
with TimerContextManager():
    # Код, время выполнения которого нужно измерить
    for i in range(1000000):
        pass


# Пример использования декоратора timer_decorator
@timer_decorator
def my_function():
    # Код, время выполнения которого нужно измерить
    for el in range(1000000):
        pass


my_function()

