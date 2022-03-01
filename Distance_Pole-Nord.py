from cmath import sqrt

POLE_NORD = 86, 172
PARIS = 48, 51, 23.81, 2, 21, 7.999

def dms_to_dd(dms):
    degv, minv, secv, degh, minh, sech = dms
    return degv + minv/60 + secv/3600, degh + minh/60 + sech/3600

def dist_dms_to_dd_pole_nord(dms):
    verti, horiz = dms_to_dd(dms)
    pnverti, pnhoriz = POLE_NORD
    return sqrt((pnverti - verti)**2 + (pnhoriz - horiz)**2)

print(dist_dms_to_dd_pole_nord(PARIS))