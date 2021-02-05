from threading import Thread
import time
from urllib.request import urlopen
from xml.etree import ElementTree


CITIES = {
    "Charlottetown": ("PE", "s0000583"),
    "Edmonton": ("AB", "s0000045"),
    "Fredericton": ("NB", "s0000250"),
    "Halifax": ("NS", "s0000318"),
    "Iqaluit": ("NU", "s0000394"),
    "Québec City": ("QC", "s0000620"),
    "Regina": ("SK", "s0000788"),
    "St. John's": ("NL", "s0000280"),
    "Toronto": ("ON", "s0000458"),
    "Victoria": ("BC", "s0000775"),
    "Whitehorse": ("YT", "s0000825"),
    "Winnipeg": ("MB", "s0000193"),
    "Yellowknife": ("NT", "s0000366"),
}


class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city
        self.province, self.code = CITIES[self.city]

    def run(self):
        url = (
            "https://dd.weather.gc.ca/citypage_weather/xml/"
            f"{self.province}/{self.code}_e.xml"
        )
        with urlopen(url) as stream:
            xml = ElementTree.parse(stream)
            self.temperature = xml.find(
                "currentConditions/temperature"
            ).text


threads = [TempGetter(c) for c in CITIES]
start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    print(f"it is {thread.temperature}°C in {thread.city}")
print(
    "Got {} temps in {} seconds".format(
        len(threads), time.time() - start
    )
)

# it is -0.7°C in Charlottetown
# it is -21.0°C in Edmonton
# it is 0.3°C in Fredericton
# it is 2.4°C in Halifax
# it is -18.4°C in Iqaluit
# it is -0.8°C in Québec City
# it is -21.0°C in Regina
# it is 8.7°C in St. John's
# it is -4.8°C in Toronto
# it is 4.7°C in Victoria
# it is -27.2°C in Whitehorse
# it is -8.3°C in Winnipeg
# it is -29.5°C in Yellowknife
# Got 13 temps in 1.7033159732818604 seconds