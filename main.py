from airports.heathrow import Heathrow
from airlines.american_airlines import ForecastKPI
from airlines.quantus import Quantus

with Heathrow() as heathrow:
    with Quantus(heathrow), ForecastKPI(heathrow):
        heathrow.set_kpis(85, "Heavy", "High")

