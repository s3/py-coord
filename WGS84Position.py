class WGS84Format:
    Degrees = 0
    DegreesMinutes = 1
    DegreesMinutesSeconds = 2

class WGS84Position:
    Latitude = 0.0
    Longitude = 0.0

    def ToString(self):
        return "%s,%s" % (self.Latitude, self.Longitude)
