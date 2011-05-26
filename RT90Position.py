import GaussKreuger
import WGS84Position


class Grid:
    RT90 = 0
    WGS84 = 1
    SWEREF99 = 2

class RT90Projection:
    rt90_7_5_gon_v = 0
    rt90_5_0_gon_v = 1
    rt90_2_5_gon_v = 2
    rt90_0_0_gon_v = 3
    rt90_2_5_gon_o = 4
    rt90_5_0_gon_o = 5



class RT90Position:
    
    def __init__(self, args):
        if len(args) == 2 and not isinstance(args[0], WGS84Position.WGS84Position):
            self.Latitude = args[0]
            self.Longitude = args[1]
            self.GridFormat = Grid.RT90
            self.Projection = RT90Projection.rt90_2_5_gon_v
            
        elif len(args) == 2 and isinstance(args[0], WGS84Position.WGS84Position):
            gkProjection = GaussKreuger()
            gkProjection.swedish_params(self.GetProjectionString(args[1]))
            lat_lon = gkProjection.geodetic_to_grid(args[0].Latitude, args[0].Longitude)
            self.Latitude = lat_lon[0]
            self.Longitude = lat_lon[1]
            self.Projection = args[1]
            
        elif len(args) == 3:
            self.Latitude = args[0]
            self.Longitude = args[1]
            self.GridFormat = Grid.RT90
            self.Projection = args[2]

    def GetProjectionString(self, projection):
        retVal = ""
        
        if projection == RT90Projection.rt90_7_5_gon_v:
            retVal = "rt90_7.5_gon_v"
        elif projection == RT90Projection.rt90_5_0_gon_v:
            retVal = "rt90_5.0_gon_v"
        elif projection == RT90Projection.rt90_2_5_gon_v:
            retVal = "rt90_2.5_gon_v"
        elif projection == RT90Projection.rt90_0_0_gon_v:
            retVal = "rt90_0.0_gon_v"
        elif projection == RT90Projection.rt90_2_5_gon_o:
            retVal = "rt90_2.5_gon_o"
        elif projection == RT90Projection.rt90_5_0_gon_o:
            retVal = "rt90_5.0_gon_o"
        else:
            retVal = "rt90_2.5_gon_v"

        return retVal


    def ToWGS84(self):
        gkProjection = GaussKreuger.GaussKreuger()
        gkProjection.swedish_params(self.GetProjectionString(self.Projection))
        lat_lon = gkProjection.grid_to_geodetic(self.Latitude, self.Longitude)

        newPos = WGS84Position.WGS84Position()
        newPos.Latitude = lat_lon[0]
        newPos.Longitude = lat_lon[1]
        newPos.GridFormat = Grid.WGS84

        return newPos

    def ToString(self):
        return "X: %s Y: %s Projection: %s" % (self.Latitude, self.Longitude, self.GetProjectionString(self.Projection))












        
    
