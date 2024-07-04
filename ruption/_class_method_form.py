from abc import ABCMeta



class ClassMethodFormMeta(ABCMeta):
    """
        Allows Class.method form useful in map/filter/etc

        assert list(map(Result.unwrap, filter(Result.is_ok, [ok(123), err("")]))) == [123]
    """

    def __new__(mcls, name, bases, namespace):
        # Create the new class
        mcls._abstract_methods = []
        cls = super().__new__(mcls, name, bases, namespace)

        abstract_methods = {
            name for name, value in namespace.items()
            if getattr(value, "__isabstractmethod__", False)
        }

        cls._abstract_methods = abstract_methods

        return cls

    def __getattribute__(cls, name: str):
        if name == "_abstract_methods" or name not in cls._abstract_methods:
            return super().__getattribute__(name)

        def dispatch_method(self, *args, **kwargs):
            return getattr(self, name)(*args, **kwargs)
        return dispatch_method
