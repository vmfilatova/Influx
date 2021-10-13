import time

from writeinflux import WriteInflux


def get_influx_time(t):
    return int(t * 1000000000)


measurement = "cluster"
data = [
    {
        "measurement": measurement,
        "time": get_influx_time(time.time()),
        "fields": {
            "pressure": "0.64"
        }
    }
]

WriteInflux(data)
