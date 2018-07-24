# To find enclosed mass within a certain radius inside the MWG
# 7-23-2018
# MSSG

import math

G = 6.7 * 10**(-11) # m^3 / (s^2 kg)
c = 3 * 10**8     # m/s
msun = 2*10**30 #kg
pi = 3.14159
kpcToMeters = 10**3  * 3.26 * 10**13 * 10**3 # m -- kpc to pc * pc to ly * ly to km (10 Tkm / ly) * km to m

# For the Sun

v = 2.2*10**5 # m/s
r = 8 * kpcToMeters  # m -- 8kpc, and 10 Tkm / ly

M = v**2 * r / G

Menc_baryonic = M/msun
print ("M enclosed in solar masses ", "{:.1e}".format(Menc_baryonic) )

# print r

####### DM
Menc = M
print ("M enclosed in kg ", "{:.1e}".format(Menc) )
rho = 6* Menc*(3./2.) / ((4./3.) * pi * (10* 12 * kpcToMeters)**3 )

print ("rho in kg / m^3 ", "{:.1e}".format(rho) )

# About right, see: assets.zombal.com/03a5cab4/GalaxyDensity.pdf

m_p = 9.11*10**(-31) * 1938  # Proton mass

print ("m_p ", "{:.1e}".format(m_p) )

####### Amount of matter

xi = Menc_baryonic*msun / ( rho * (4./3.) * pi * (8 * kpcToMeters)**3 ) 

print ("ratio of baryonic to DM within solar circle ",  "{:.1e}".format(xi) )

