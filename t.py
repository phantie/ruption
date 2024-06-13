class Result(Generic[Ok, Err], metaclass=ABCMeta):
    # https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap
    @abstractmethod
    def unwrap(self) -> Ok:
        """
            returns inner value if ok
            panics if err
        """

class ok(Result[Ok, Err]):
    def unwrap(self) -> Ok:
        return self.T

class err(Result[Ok, Err]):
    def unwrap(self) -> NoReturn:
        raise Panic("called .unwrap() on err")