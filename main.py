# -*- coding: cp1252 -*-
import WGS84Position
import SWEREF99Position
import RT90Position


# Alla argument till konstruktorerna för de olika koordinaterna måste ges som listor
# :D


if __name__ == "__main__":
        
    # RT90 tar 2 koordinater och eventuellt en projection av dessa som 3e argument:
    ##    rt90_7_5_gon_v = 0
    ##    rt90_5_0_gon_v = 1
    ##    rt90_2_5_gon_v = 2
    ##    rt90_0_0_gon_v = 3
    ##    rt90_2_5_gon_o = 4
    ##    rt90_5_0_gon_o = 5
    
    rt90a = RT90Position.RT90Position([6579749, 1632937])
    
    # som default används rt90_2_5_gon_v, så ovanstående är samma som
    rt90b = RT90Position.RT90Position([6579749, 1632937, 2])

    # bevis jao:
    print "rt90a: " + rt90a.ToWGS84().ToString()
    print "rt90b: " + rt90b.ToWGS84().ToString()

    # utdata från ToString() kan köttas in i google maps direkt

    # ------------------------
    # SWEREF99 har 12 olika projections, som default används 0:
    ##    sweref_99_tm = 0
    ##    sweref_99_12_00 = 1
    ##    sweref_99_13_30 = 2
    ##    sweref_99_15_00 = 3
    ##    sweref_99_16_30 = 4
    ##    sweref_99_18_00 = 5
    ##    sweref_99_14_15 = 6
    ##    sweref_99_15_45 = 7
    ##    sweref_99_17_15 = 8
    ##    sweref_99_18_45 = 9
    ##    sweref_99_20_15 = 10
    ##    sweref_99_21_45 = 11
    ##    sweref_99_23_15 = 12

    sweref = SWEREF99Position.SWEREF99Position([6579634,678689])
    print "sweref: " + sweref.ToWGS84().ToString()
