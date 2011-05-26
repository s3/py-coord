import GaussKreuger
import WGS84Position

class Grid:
    RT90 = 0
    WGS84 = 1
    SWEREF99 = 2

class SWEREFProjection:
    sweref_99_tm = 0
    sweref_99_12_00 = 1
    sweref_99_13_30 = 2
    sweref_99_15_00 = 3
    sweref_99_16_30 = 4
    sweref_99_18_00 = 5
    sweref_99_14_15 = 6
    sweref_99_15_45 = 7
    sweref_99_17_15 = 8
    sweref_99_18_45 = 9
    sweref_99_20_15 = 10
    sweref_99_21_45 = 11
    sweref_99_23_15 = 12


class SWEREF99Position:
    SWEREFProjections = ["sweref_99_tm",
                         "sweref_99_12_00",
                         "sweref_99_13_30",
                         "sweref_99_15_00",
                         "sweref_99_16_30",
                         "sweref_99_18_00",
                         "sweref_99_14_15",
                         "sweref_99_15_45",
                         "sweref_99_17_15",
                         "sweref_99_18_45",
                         "sweref_99_20_15",
                         "sweref_99_21_45",
                         "sweref_99_23_15"]

    def __init__(self, args):
        if len(args) == 2:
            self.Latitude = args[0]
            self.Longitude = args[1]
            self.GridFormat = Grid.SWEREF99
            self.Projection = SWEREFProjection.sweref_99_tm
        elif len(args) == 3:
            self.Latitude = args[0]
            self.Longitude = args[1]
            self.GridFormat = Grid.SWEREF99
            self.Projection = args[2]


    def ToWGS84(self):
        gkProjection = GaussKreuger.GaussKreuger()
        gkProjection.swedish_params(self.SWEREFProjections[self.Projection])
        lat_lon = gkProjection.grid_to_geodetic(self.Latitude, self.Longitude)

        newPos = WGS84Position.WGS84Position()
        newPos.Latitude = lat_lon[0]
        newPos.Longitude = lat_lon[1]
        newPos.GridFormat = Grid.WGS84

        return newPos


    def ToString(self):
        return "N: %s E: %s Projection: %s" % (self.Latitude, self.Longitude, self.SWEREFProjections[self.Projection])













    
            
            
