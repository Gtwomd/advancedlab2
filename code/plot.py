from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

Y, scattering, scattering_and_wall = np.loadtxt('../data/rutherford.txt', unpack=True)


N_2 = scattering_and_wall/600
delta_N_2 = np.power(scattering_and_wall,1/2)/600
N_2_minus_wall = scattering/600
delta_N_2_minus_wall = np.power(scattering,1/2)/600

theory_Y= np.loadtxt('theory_Y')
theory_scattering = np.loadtxt('theory_scattering')

fig, ax = plt.subplots()

N_0_times_G = 0.17

ax.plot(100*theory_Y, N_0_times_G*theory_scattering, label="Prediction\nwith $N_0*G={:.2f}$".format(N_0_times_G))
ax.errorbar(Y, N_2, delta_N_2, marker='o',ls='', label='Measurement')
ax.set_ylabel('scattering $N_2$')
ax.set_xlabel('$Y$ (cm)')
ax.legend(loc=4)
plt.savefig('../figures/N_2_prediction_and_data.pdf')
