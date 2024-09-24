import abc


class AbsObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, value):
        pass

    def __enter__(self):
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class AbsSubject(metaclass=abc.ABCMeta):
    _observer = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError("Unknown object")
        self._observer |= {observer}

    def detach(self, observer):
        self._observer -= {observer}

    def notify(self, value=None):
        for observer in self._observer:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observer.clear()


class KPI(AbsSubject):
    open_ticket = -1
    close_ticket = -1
    new_ticket = -1

    def __init__(self):
        print("I'm called")

    @property
    def open(self):
        return self.open_ticket

    @property
    def close(self):
        return self.close_ticket

    @property
    def new(self):
        return self.new_ticket

    def set_kpi(self, open, closed, new):
        self.open_ticket = open
        self.close_ticket = closed
        self.new_ticket = new
        self.notify()


class CurrentKPS(AbsObserver):
    open_ticket = -1
    close_ticket = -1
    new_ticket = -1

    def __init__(self, kpi):
        self._kpi = kpi
        kpi.attach(self)

    def update(self):
        self.open_ticket = self._kpi.open
        self.close_ticket = self._kpi.close
        self.new_ticket = self._kpi.new
        self.display()

    def display(self):
        print(self.open_ticket)
        print(self.close_ticket)
        print(self.new_ticket)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpi.detach(self)


class ForcastKPS(AbsObserver):
    open_ticket = -1
    close_ticket = -1
    new_ticket = -1

    def __init__(self, kpi):
        self._kpi = kpi
        kpi.attach(self)

    def update(self):
        self.open_ticket = self._kpi.open
        self.close_ticket = self._kpi.close
        self.new_ticket = self._kpi.new
        self.display()

    def display(self):
        print(self.open_ticket)
        print(self.close_ticket)
        print(self.new_ticket)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpi.detach(self)


with KPI() as kpi:
    with CurrentKPS(kpi), ForcastKPS(kpi):
        kpi.set_kpi(10, 20, 30)