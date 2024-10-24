from airlines.abs_airline import AbsObserver


class ForecastKPI(AbsObserver):
    wind_speed = -1
    rain_fall = ""
    risk_of_hail = ""

    def __init__(self, kpi):
        self._kpi = kpi
        kpi.attach(self)

    def update(self):
        self.wind_speed = self._kpi.wind_speed
        self.rain_fall = self._kpi.rain_fall
        self.risk_of_hail = self._kpi.risk_of_hail
        self.display()

    def display(self):
        print("American Airline Flights please observe: flights please observe: "
              "{} reports {} knot winds"
              .format(self._kpi.__class__.__name__, self.wind_speed))
        print("QAmerican Airline Flights please observe: flights please observe: "
              "{} reports a {} chance of rain"
              .format(self._kpi.__class__.__name__, self.rain_fall))
        print("American Airline Flights please observe: flights please observe: "
              "{} reports {} chance of hail"
              .format(self._kpi.__class__.__name__, self.risk_of_hail))
        print("*" * 20)


    def __exit__(self, exc_type, exc_val, exc_tb):
        self._kpi.detach(self)