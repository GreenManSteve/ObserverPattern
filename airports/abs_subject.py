import abc

from airlines.abs_airline import AbsObserver


class AbsSubject(metaclass=abc.ABCMeta):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError("Not an expected observer")
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()