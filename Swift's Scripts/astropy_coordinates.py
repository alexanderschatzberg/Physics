# Defining a SkyCoord object
from astropy.coordinates import get_sun
import matplotlib.pyplot as plt
import numpy as np
from astropy.time import Time
from astropy.coordinates import FK5
from astropy import units as u
from astropy.coordinates import SkyCoord

c = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')

# Accessing attributes
c.ra
c.ra.hour
c.ra.hms
c.dec
c.dec.degree
c.dec.radian

# Coordinate transformation
c_icrs = SkyCoord(ra=10.68458*u.degree, dec=41.26917*u.degree, frame='icrs')
c_icrs.galactic

c_fk5 = c_icrs.transform_to('fk5')  # c_icrs.fk5 does the same thing
c_fk5


c_fk5.transform_to(FK5(equinox='J1975'))  # precess to a different equinox

# Coordinate separation
c1 = SkyCoord(ra=10*u.degree, dec=9*u.degree, frame='icrs')
c2 = SkyCoord(ra=11*u.degree, dec=10*u.degree, frame='fk5')
sep = c1.separation(c2)  # Differing frames handled correctly
sep.arcmin


# Sun position
t1 = Time('2022-9-23 21:00:00')
sun = get_sun(t1)
sun.dec

# Where would you expect the Sun to be on the Equinox?
t2 = Time('2022-09-22 12:00:00')
sun = get_sun(t2)
sun.dec


# Sun's path across the celestial sphere
tdelta = np.linspace(0, 365, 365)*u.day

time = t2 + tdelta

sunra = []
sundec = []
for t in time:
    sun = get_sun(t)
    sundec = np.append(sundec, sun.dec.degree)
    sunra = np.append(sunra, sun.ra.hour)


plt.ion()
plt.figure()
plt.clf()
plt.plot(sunra, sundec, 'k.')
plt.xlim(0, 24)
plt.xlabel('Sun RA (hours)')
plt.ylabel('Sun Dec (degrees)')
plt.title('Celestial Coordinates of the Sun Over 1 Year')

plt.savefig('Sun_RA_Dec.png', dpi=300)
