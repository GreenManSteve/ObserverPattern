from airports.abs_subject import AbsSubject


class Heathrow(AbsSubject):
    _wind_speed = 85
    _rain_fall = "Heavy"
    _risk_of_hail = "High"

    @property
    def wind_speed(self):
        return self._wind_speed

    @property
    def rain_fall(self):
        return self._rain_fall

    @property
    def risk_of_hail(self):
        return self._risk_of_hail

    def set_kpis(self, wind_speed, rain_fall, risk_of_hail):
        self._wind_speed = wind_speed
        self._rain_fall = rain_fall
        self._risk_of_hail = risk_of_hail
        self.notify()
