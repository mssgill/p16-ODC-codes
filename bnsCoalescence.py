# MSSG
# 7-18-2018
# To calculate the time to coalescence of a BNS, using numbers for the Hulse-Taylor binary
# see: https://en.wikipedia.org/wiki/Gravitational_wave#Binaries  for the form of the eq
# see: https://en.wikipedia.org/wiki/Hulse%E2%80%93Taylor_binary for the 300Myr to merger number


import math

G = 6.7 * 10**(-11) # MKS
c = 3 * 10**8     # m/s

msun = 2*10**30 #kg

m1 = 1.4 * msun
m2 = 1.4 * msun

rsun = 7*10**8 # m

r = 1.8 * rsun
tconv = 3*10**7

t = (5./ 256.)* (c**5 /G**3) * r**4 / (( m1* m2 ) * ( m1 + m2 )) / tconv

print(t)

print("Time in yrs to coalescence ", "{:.1e}".format(t))

