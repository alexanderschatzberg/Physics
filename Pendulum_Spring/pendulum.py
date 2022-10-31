import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.distributions import chi2
from scipy.optimize import curve_fit

######################################################################
# For testing effect of amplitude on period
# amplitude (degrees)
#!!! ENTER DATA HERE !!!#
amplitude = np.array(['enter data as floats, comma separated'])
# estimated error on amplitude
eamplitude = np.array([])
# period (seconds)
period_a = np.array([])
# estimated error on period
eperiod_a = np.array([])


######################################################################
# For testing effect of mass on period
#!!! ENTER DATA HERE !!!#
mass = np.array([])
emass = np.array([])
period_m = np.array([])
eperiod_m = np.array([])


######################################################################
# For testing effect of mass on period
# length in centimeters
#!!! ENTER DATA HERE !!!#
length = np.array([])
elength = np.array([])
period_l = np.array([])
eperiod_l = np.array([])


#################################################################XS#####
# Make some plots!
plt.ion()
plt.figure(1)
plt.clf()
plt.errorbar(amplitude, period_a, xerr=eamplitude, yerr=eperiod_a, fmt='o')
plt.xlabel('Amplitude (deg))', fontsize=14)
plt.ylabel('Period (s)', fontsize=16)
# Set the proper limits for the graph
plt.xlim(0, 40)
plt.ylim(0, 2)
plt.title('Period vs. Amplitude', fontsize=16)
# When you are happy with the way the plot looks, you can uncomment the following line to save it to your disk
# plt.savefig('Period_vs_Amplitude.png',dpi=300)

meanp_a = np.average(period_a, weights=1/eperiod_a**2)
chisqa = (period_a-meanp_a)**2/eperiod_a**2
print('Chi-squared p-value for a flat line model:')
chi2.sf(np.sum(chisqa), len(period_a))


######################################################################
# Period vs. Mass
plt.figure(2)
plt.clf()
plt.errorbar(mass, period_m, xerr=emass, yerr=eperiod_m, fmt='o')
plt.xlabel('Mass (g))', fontsize=14)
plt.ylabel('Period (s)', fontsize=16)
# Set the proper limits for the graph
plt.xlim(0, 350)
plt.ylim(0, 2)
plt.title('Period vs. Mass', fontsize=16)
# When you are happy with the way the plot looks, you can uncomment the following line to save it to your disk
# plt.savefig('Period_vs_Mass.png',dpi=300)


meanp_m = np.average(period_m, weights=1/eperiod_m**2)
chisqm = (period_m-meanp_m)**2/eperiod_m**2
print('Chi-squared p-value for a flat line model:')
chi2.sf(np.sum(chisqm), len(period_m))


######################################################################
# Period vs. Length
plt.figure(3)
plt.clf()
plt.errorbar(length, period_l, xerr=elength, yerr=eperiod_l, fmt='o')
plt.xlabel('Length (cm)', fontsize=14)
plt.ylabel('Period (s)', fontsize=16)
# Set the proper limits for the graph
plt.xlim(0, 100)
plt.ylim(0, 3)
plt.title('Period vs. Length', fontsize=16)
# When you are happy with the way the plot looks, you can uncomment the following line to save it to your disk
# plt.savefig('Period_vs_Length.png',dpi=300)

meanp_l = np.average(period_l, weights=1/eperiod_l**2)
chisql = (period_l-meanp_l)**2/eperiod_l**2
print('Chi-squared p-value for a flat line model:')
chi2.sf(np.sum(chisql), len(period_l))


# What relationship do you think might best describe the data? Let's first try a line
# a line
def func1(x, m, b):
    return m*x + b


# Fit a line to the data
popt1, pcov1 = curve_fit(func1, length, period_l, sigma=eperiod_l)

plt.figure(4)
plt.clf()
plt.errorbar(length, period_l, xerr=elength, yerr=eperiod_l, fmt='o')
plt.xlabel('Length (cm)', fontsize=14)
plt.ylabel('Period (s)', fontsize=16)
# Set the proper limits for the graph
plt.xlim(0, 100)
plt.ylim(0, 3)

# Overplot the best fitting model
xfit1 = np.linspace(plt.xlim()[0], plt.xlim()[1], 1000)
yfit1 = func1(xfit1, popt1[0], popt1[1])
plt.plot(xfit1, yfit1, 'r--')

plt.title('Period vs. Length (with linear fit)', fontsize=16)
# When you are happy with the way the plot looks, you can uncomment the following line to save it to your disk
# plt.savefig('Period_vs_Length_line.png',dpi=300)


chisqline = (period_l-func1(length, popt1[0], popt1[1]))**2/eperiod_l**2
print('Chi-squared p-value for a linear model:')
chi2.sf(np.sum(chisqline), len(period_l))


# Maybe try a different functional form...
#!!! ENTER YOUR CUSTOM FUNCTION HERE !!!
def func2(x, g):
    return


# Fit your custom function to the data
popt2, pcov2 = curve_fit(func2, length, period_l, sigma=eperiod_l)

# Does this fit the data well?
popt2[0], np.sqrt(pcov2[0])

plt.figure(5)
plt.clf()
plt.errorbar(length, period_l, xerr=elength, yerr=eperiod_l, fmt='o')
plt.xlabel('Length (cm)', fontsize=14)
plt.ylabel('Period (s)', fontsize=16)
# Set the proper limits for the graph
plt.xlim(0, 100)
plt.ylim(0, 3)

# Overplot the best fitting model
xfit2 = np.linspace(plt.xlim()[0], plt.xlim()[1], 1000)
yfit2 = func2(xfit2, popt2[0])
plt.plot(xfit2, yfit2, 'r--')

plt.title('Period vs. Length (with XXX fit)', fontsize=16)
# When you are happy with the way the plot looks, you can uncomment the following line to save it to your disk
# plt.savefig('Period_vs_Length_XXX.png',dpi=300)

chisqcustom = (period_l-func2(length, popt2[0]))**2/eperiod_l**2
print('Chi-squared p-value for your custom model:')
chi2.sf(np.sum(chisqcustom), len(period_l))
