import math

class GaussKreuger:
    axis, flattening, central_meridian, scale, \
    false_northing, false_easting = (None,None,None,None,None,None)

    def swedish_params(self, projection):
        # RT90 parameters, GRS 80 ellipsoid.
        if (projection == "rt90_7.5_gon_v"):
            self.grs80_params()
            self.central_meridian = 11.0 + 18.375 / 60.0
            self.scale = 1.000006000000
            self.false_northing = -667.282
            self.false_easting = 1500025.141
        
        elif (projection == "rt90_5.0_gon_v"):
            self.grs80_params()
            self.central_meridian = 13.0 + 33.376 / 60.0
            self.scale = 1.000005800000
            self.false_northing = -667.130
            self.false_easting = 1500044.695
        
        elif (projection == "rt90_2.5_gon_v"):
            self.grs80_params()
            self.central_meridian = 15.0 + 48.0 / 60.0 + 22.624306 / 3600.0
            self.scale = 1.00000561024
            self.false_northing = -667.711
            self.false_easting = 1500064.274
        
        elif (projection == "rt90_0.0_gon_v"):
            self.grs80_params()
            self.central_meridian = 18.0 + 3.378 / 60.0
            self.scale = 1.000005400000
            self.false_northing = -668.844
            self.false_easting = 1500083.521
        
        elif (projection == "rt90_2.5_gon_o"):
            self.grs80_params()
            self.central_meridian = 20.0 + 18.379 / 60.0
            self.scale = 1.000005200000
            self.false_northing = -670.706
            self.false_easting = 1500102.765
        
        elif (projection == "rt90_5.0_gon_o"):
            self.grs80_params()
            self.central_meridian = 22.0 + 33.380 / 60.0
            self.scale = 1.000004900000
            self.false_northing = -672.557
            self.false_easting = 1500121.846
        

        # RT90 parameters, Bessel 1841 ellipsoid.
        elif (projection == "bessel_rt90_7.5_gon_v"):
            self.bessel_params()
            self.central_meridian = 11.0 + 18.0 / 60.0 + 29.8 / 3600.0
        
        elif (projection == "bessel_rt90_5.0_gon_v"):
            self.bessel_params()
            self.central_meridian = 13.0 + 33.0 / 60.0 + 29.8 / 3600.0
        
        elif (projection == "bessel_rt90_2.5_gon_v"):
            self.bessel_params()
            self.central_meridian = 15.0 + 48.0 / 60.0 + 29.8 / 3600.0
        
        elif (projection == "bessel_rt90_0.0_gon_v"):
            self.bessel_params()
            self.central_meridian = 18.0 + 3.0 / 60.0 + 29.8 / 3600.0
        
        elif (projection == "bessel_rt90_2.5_gon_o"):
            self.bessel_params()
            self.central_meridian = 20.0 + 18.0 / 60.0 + 29.8 / 3600.0
        
        elif (projection == "bessel_rt90_5.0_gon_o"):
            self.bessel_params()
            self.central_meridian = 22.0 + 33.0 / 60.0 + 29.8 / 3600.0
        

        # SWEREF99TM and SWEREF99ddmm  parameters.
        elif (projection == "sweref_99_tm"):
            self.sweref99_params()
            self.central_meridian = 15.00
            self.scale = 0.9996
            self.false_northing = 0.0
            self.false_easting = 500000.0
        
        elif (projection == "sweref_99_1200"):
            self.sweref99_params()
            self.central_meridian = 12.00
        
        elif (projection == "sweref_99_1330"):
            self.sweref99_params()
            self.central_meridian = 13.50
        
        elif (projection == "sweref_99_1500"):
            self.sweref99_params()
            self.central_meridian = 15.00
        
        elif (projection == "sweref_99_1630"):
            self.sweref99_params()
            self.central_meridian = 16.50
        
        elif (projection == "sweref_99_1800"):
            self.sweref99_params()
            self.central_meridian = 18.00
        
        elif (projection == "sweref_99_1415"):
            self.sweref99_params()
            self.central_meridian = 14.25
        
        elif (projection == "sweref_99_1545"):
            self.sweref99_params()
            self.central_meridian = 15.75
        
        elif (projection == "sweref_99_1715"):
            self.sweref99_params()
            self.central_meridian = 17.25
        
        elif (projection == "sweref_99_1845"):
            self.sweref99_params()
            self.central_meridian = 18.75
        
        elif (projection == "sweref_99_2015"):
            self.sweref99_params()
            self.central_meridian = 20.25
        
        elif (projection == "sweref_99_2145"):
            self.sweref99_params()
            self.central_meridian = 21.75
        
        elif (projection == "sweref_99_2315"):
            self.sweref99_params()
            self.central_meridian = 23.25
        
        else:
            self.central_meridian = 31337.0


    #Sets of default parameters.
    def grs80_params(self):
        self.axis = 6378137.0 # GRS 80.
        self.flattening = 1.0 / 298.257222101 # GRS 80.
        self.central_meridian = 31337.0

    def bessel_params(self):
        self.axis = 6377397.155 # Bessel 1841.
        self.flattening = 1.0 / 299.1528128 # Bessel 1841.
        self.central_meridian = 31337.0
        self.scale = 1.0
        self.false_northing = 0.0
        self.false_easting = 1500000.0

    def sweref99_params(self):
        self.axis = 6378137.0 # GRS 80.
        self.flattening = 1.0 / 298.257222101 # GRS 80.
        self.central_meridian = 31337.0
        self.scale = 1.0
        self.false_northing = 0.0
        self.false_easting = 150000.0



    # Conversion from geodetic coordinates to grid coordinates.
    def geodetic_to_grid(self, latitude, longitude):
        x_y = [0.0, 0.0]

        # Prepare ellipsoid-based stuff.
        e2 = self.flattening * (2.0 - self.flattening)
        n = self.flattening / (2.0 - self.flattening)
        a_roof = self.axis / (1.0 + n) * (1.0 + n * n / 4.0 + n * n * n * n / 64.0)
        A = e2
        B = (5.0 * e2 * e2 - e2 * e2 * e2) / 6.0
        C = (104.0 * e2 * e2 * e2 - 45.0 * e2 * e2 * e2 * e2) / 120.0
        D = (1237.0 * e2 * e2 * e2 * e2) / 1260.0
        beta1 = n / 2.0 - 2.0 * n * n / 3.0 + 5.0 * n * n * n / 16.0 + 41.0 * n * n * n * n / 180.0
        beta2 = 13.0 * n * n / 48.0 - 3.0 * n * n * n / 5.0 + 557.0 * n * n * n * n / 1440.0
        beta3 = 61.0 * n * n * n / 240.0 - 103.0 * n * n * n * n / 140.0
        beta4 = 49561.0 * n * n * n * n / 161280.0

        # Convert.
        deg_to_rad = math.pi / 180.0
        phi = latitude * deg_to_rad
        lambd = longitude * deg_to_rad
        lambda_zero = self.central_meridian * deg_to_rad

        phi_star = phi - math.sin(phi) * math.cos(phi) * (A + \
                        B * math.pow(math.sin(phi), 2) + \
                        C * math.pow(math.sin(phi), 4) + \
                        D * math.pow(math.sin(phi), 6))
        delta_lambda = lambd - lambda_zero
        xi_prim = math.atan(math.tan(phi_star) / math.cos(delta_lambda))
        eta_prim = math.atanh(math.cos(phi_star) * math.sin(delta_lambda))
        x = self.scale * a_roof * (xi_prim + \
                        beta1 * math.sin(2.0 * xi_prim) * math.cosh(2.0 * eta_prim) + \
                        beta2 * math.sin(4.0 * xi_prim) * math.cosh(4.0 * eta_prim) + \
                        beta3 * math.sin(6.0 * xi_prim) * math.cosh(6.0 * eta_prim) + \
                        beta4 * math.sin(8.0 * xi_prim) * math.cosh(8.0 * eta_prim)) + \
                        self.false_northing
        y = self.scale * a_roof * (eta_prim + \
                        beta1 * math.cos(2.0 * xi_prim) * math.sinh(2.0 * eta_prim) + \
                        beta2 * math.cos(4.0 * xi_prim) * math.sinh(4.0 * eta_prim) + \
                        beta3 * math.cos(6.0 * xi_prim) * math.sinh(6.0 * eta_prim) + \
                        beta4 * math.cos(8.0 * xi_prim) * math.sinh(8.0 * eta_prim)) + \
                        self.false_easting
        x_y[0] = round(x * 1000.0) / 1000.0
        x_y[1] = round(y * 1000.0) / 1000.0

        return x_y


    def grid_to_geodetic(self, x, y):
        lat_lon = [0.0, 0.0]
        
        if (self.central_meridian == 31337.0):
            return lat_lon

        # Prepare ellipsoid-based stuff.
        e2 = self.flattening * (2.0 - self.flattening)
        n = self.flattening / (2.0 - self.flattening)
        a_roof = self.axis / (1.0 + n) * (1.0 + n * n / 4.0 + n * n * n * n / 64.0)
        delta1 = n / 2.0 - 2.0 * n * n / 3.0 + 37.0 * n * n * n / 96.0 - n * n * n * n / 360.0
        delta2 = n * n / 48.0 + n * n * n / 15.0 - 437.0 * n * n * n * n / 1440.0
        delta3 = 17.0 * n * n * n / 480.0 - 37 * n * n * n * n / 840.0
        delta4 = 4397.0 * n * n * n * n / 161280.0

        Astar = e2 + e2 * e2 + e2 * e2 * e2 + e2 * e2 * e2 * e2
        Bstar = -(7.0 * e2 * e2 + 17.0 * e2 * e2 * e2 + 30.0 * e2 * e2 * e2 * e2) / 6.0
        Cstar = (224.0 * e2 * e2 * e2 + 889.0 * e2 * e2 * e2 * e2) / 120.0
        Dstar = -(4279.0 * e2 * e2 * e2 * e2) / 1260.0

        # Convert.
        deg_to_rad = math.pi / 180
        lambda_zero = self.central_meridian * deg_to_rad
        xi = (x - self.false_northing) / (self.scale * a_roof)
        eta = (y - self.false_easting) / (self.scale * a_roof)
        xi_prim = xi - \
                        delta1 * math.sin(2.0 * xi) * math.cosh(2.0 * eta) - \
                        delta2 * math.sin(4.0 * xi) * math.cosh(4.0 * eta) - \
                        delta3 * math.sin(6.0 * xi) * math.cosh(6.0 * eta) - \
                        delta4 * math.sin(8.0 * xi) * math.cosh(8.0 * eta)
        eta_prim = eta - \
                        delta1 * math.cos(2.0 * xi) * math.sinh(2.0 * eta) - \
                        delta2 * math.cos(4.0 * xi) * math.sinh(4.0 * eta) - \
                        delta3 * math.cos(6.0 * xi) * math.sinh(6.0 * eta) - \
                        delta4 * math.cos(8.0 * xi) * math.sinh(8.0 * eta)
        phi_star = math.asin(math.sin(xi_prim) / math.cosh(eta_prim))
        delta_lambda = math.atan(math.sinh(eta_prim) / math.cos(xi_prim))
        lon_radian = lambda_zero + delta_lambda
        lat_radian = phi_star + math.sin(phi_star) * math.cos(phi_star) * \
                        (Astar + \
                         Bstar * math.pow(math.sin(phi_star), 2) + \
                         Cstar * math.pow(math.sin(phi_star), 4) + \
                         Dstar * math.pow(math.sin(phi_star), 6))
        lat_lon[0] = lat_radian * 180.0 / math.pi
        lat_lon[1] = lon_radian * 180.0 / math.pi
        return lat_lon


