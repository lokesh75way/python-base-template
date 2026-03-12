from typing import TypeVar, Generic, Type, Any

T = TypeVar("T")

class _SingletonWrapper(Generic[T]):
    """
    A singleton wrapper class. Its instances would be created
    for each decorated class.
    """

    def __init__(self, cls: Type[T]):
        self.__wrapped__: Type[T] = cls
        self._instance: T | None = None

    def __call__(self, *args: Any, **kwargs: Any) -> T:
        """Returns a single instance of decorated class"""
        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)
        return self._instance

def singleton(cls: Type[T]) -> _SingletonWrapper[T]:
    """
    A singleton decorator. Returns a wrapper object. A call on that object
    returns a single instance object of decorated class.
    Use the __wrapped__ attribute to access decorated class directly in unit tests.
    """
    return _SingletonWrapper(cls)
