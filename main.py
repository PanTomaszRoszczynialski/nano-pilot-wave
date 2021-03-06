from subprocess import call
from matplotlib import pyplot as plt
import numpy as np
import os
import anal as an
import pickle

template_file   = 'in.pilot_template.lamps'
oscillator_file = 'in.oscillators.lamps'
ference_file    = 'in.interference.lamps'

class LampsRunner(object):
    """ Convenience class for running lammps fro python """
    def __init__(self):
	""" Co robi traktor u fryzjera? Warkocze """
	self.gravity_marker	 = 'GRAVITY'
	self.gravity             = '8.5'
	self.frequency_marker    = 'MEMBRANE_FREQUENCY'
	self.membrane_frequency  = '1100'
        self.amp_marker          = 'AMPLITUDE'
        self.amplitude           = '0.33'
        self.a_ball_z_marker     = 'A_BALL_HEIGHT'
        self.a_ball_z            = '-6.2'
        self.spring_marker       = 'SPRING_CONSTANT'
        self.spring_factor       = '0.5'
        self.a_mass_marker       = 'A_BALL_MASS'
        self.a_mass              = '392.01'
        self.iterations_marker   = 'ITERATIONS'
        self.iterations          = '20000'
        self.sheet_radius_m      = 'SHEET_RADIUS'
        self.sheet_radius        = '88'
        self.mb_bond_marker      = 'MEM_K'
        self.mb_bond_k           = '0.6'
        self.mb_bond_r0_marker   = 'MEM_R0'
        self.mb_bond_r0          = '1.1'
        self.processes           = '8'
        self.a_ball_x_m          = 'a_ball_x'
        self.a_ball_x            = '10'
        self.a_ball_y_m          = 'a_ball_y'
        self.a_ball_y            = '10'
        self.a_ball_y_vel_m      = 'a_ball_y_vel'
        self.a_ball_y_vel        = '0.013'

        self.silent              = True

    def set_membrane_bond_harmonic_constant(self, kz):
        """ wow """
        self.mb_bond_k = str(kz)

    def set_mb_bond_r(self, angstroms):
        """ Equilibrium distance """
        self.mb_bond_r0 = str(angstroms)

    def set_number_of_cores(self, howmany):
        """ how """
        self.processes = str(howmany)

    def set_sheet_radius(self, nm):
        """ this is necessary """
        self.sheet_radius = str(nm)

    def set_number_of_iterations(self, howmany):
        """ how long """
        self.iterations = str(howmany)

    def set_spring_constant(self, k):
        """ wtf units """
        self.spring_factor = str(k)

    def set_a_ball_height(self, angstroms):
        """ how high """
        self.a_ball_z = str(angstroms)

    def set_amplitude(self, amp):
        """ futro odrosnie jutro """
        self.amplitude = str(amp)

    def set_a_ball_mass(self, kg):
        """ time of flight should not be related to the mass """
        self.a_mass = str(kg)

    def set_gravity(self, grav):
	""" kontempluj przejaw tao """
	self.gravity = str(grav)

    def set_membrane_frequency(self, freq):
	""" set me """
	self.membrane_frequency = str(freq)

    def set_a_ball_y(self, y):
        """ STarting position x """
        self.a_ball_y = str(y)

    def set_a_ball_x(self, x):
        """ STarting position x """
        self.a_ball_x = str(x)

    def set_a_ball_y_vel(self, vel):
        """ Starting velocity """
        self.a_ball_y_vel = str(vel)

    def set_silent(self, isit):
        """ lammps thermos on/off """
        self.silent = isit

    def run_it(self, filepath):
	""" Runs lammps """
        # Unix mp-ready version
	commands = ['mpirun', '-np', self.processes,
                    'lammps-daily',
                    '-var', self.amp_marker, self.amplitude,
                    '-var', self.gravity_marker, self.gravity,
                    '-var', self.spring_marker, self.spring_factor,
                    '-var', self.a_ball_z_marker, self.a_ball_z,
                    '-var', self.frequency_marker, self.membrane_frequency,
                    '-var', self.a_mass_marker, self.a_mass,
                    '-var', self.sheet_radius_m, self.sheet_radius,
                    '-var', self.iterations_marker, self.iterations,
                    '-var', self.mb_bond_marker, self.mb_bond_k,
                    '-var', self.mb_bond_r0_marker, self.mb_bond_r0,
                    '-var', self.a_ball_x_m, self.a_ball_x,
                    '-var', self.a_ball_y_m, self.a_ball_y,
                    '-var', self.a_ball_y_vel_m, self.a_ball_y_vel,
                    '-in', filepath]

        # Windows slow version
	commands2= ['lmp_serial', '-i', filepath,
                    '-var', self.amp_marker, self.amplitude,
                    '-var', self.gravity_marker, self.gravity,
                    '-var', self.spring_marker, self.spring_factor,
                    '-var', self.a_ball_z_marker, self.a_ball_z,
                    '-var', self.frequency_marker, self.membrane_frequency,
                    '-var', self.a_mass_marker, self.a_mass,
                    '-var', self.sheet_radius_m, self.sheet_radius,
                    '-var', self.mb_bond_marker, self.mb_bond_k,
                    '-var', self.iterations_marker, self.iterations,
                    '-var', self.mb_bond_r0_marker, self.mb_bond_r0,
                    '-var', self.a_ball_y_m, self.a_ball_y,
                    '-var', self.a_ball_x_m, self.a_ball_x
                    ]

        if self.silent:
            call(commands, stdout=open(os.devnull, 'wb'))
        else:
            # Verbose
            call(commands)

if __name__ == '__main__':
    """ Run lammps multiple times with python main.py """

    runner = LampsRunner()

    # Membrane driving force frequency
    frequencies     = 1000
    runner.set_membrane_frequency(frequencies)

    # Drop the ball from
    a_ball_zs       = -7.6
    runner.set_a_ball_height(a_ball_zs)

    # Driving force amplitude
    amplitudes      = 0.05
    runner.set_amplitude(amplitudes)

    # Membrane size
    sheet_radius    = 70
    runner.set_sheet_radius(sheet_radius)

    # And x
    x_position = 150
    runner.set_a_ball_x(x_position)

    # Membrane bonds equilibric distances
    membrane_r_zeros = 1.1
    runner.set_mb_bond_r(membrane_r_zeros)

    # Starting velocity
    y_velocity = 0.0
    runner.set_a_ball_y_vel(y_velocity)

    # Ball starting postion-y
    y_position = 150
    runner.set_a_ball_y(y_position)

    # Freefall force (13.01)
    gravity         = 43.1
    runner.set_gravity(gravity)

    # 102.01 and 112.01 gave great results (404)
    a_ball_mass     = [320.2 + 0.0005 * it for it in range(60)][6]
    runner.set_a_ball_mass(a_ball_mass)

    # Membrane harmonic constant 1.36
    membrane_bond_ks = 1.36
    runner.set_membrane_bond_harmonic_constant(membrane_bond_ks)

    # Spring constant of the membrane points 1.12
    spring_factors  = 1.076
    runner.set_spring_constant(spring_factors)

    # Declare score paths
    ball_file = 'data/a_ball.dat'
    memb_file = 'data/membrane_pos.dat'

    # Prepare score containers
    ball_pos    = []
    membranes_z = []

    # Final settings
    runner.set_silent(False)
    runner.set_number_of_iterations(int(1e8))
    runner.set_number_of_cores(8)

    for val in range(1):
        print 'current value is now set to: ', val
        # Set value to check and check

        # Run
        runner.run_it(ference_file)

        # Write ball positions
        ball_score = an.read_pos(ball_file)
        ball_pos.append(ball_score)

        # Membrane as well
        memb_score = an.read_pos(memb_file)
        mz = [pos[2] for pos in memb_score]
        membranes_z.append(mz)

        # Save histogram after each run
        # savepath = 'plots/start_position/x_pos{}.png'.format(val)
        # an.make_position_histogram(ball_file, limits=[130, 170], savepath=savepath)

        # Resave every iteration (you can see those live with ipython)
        with open('data/ball.pickle', 'wb') as fout:
            pickle.dump(ball_pos, fout)
        with open('data/memb.pickle', 'wb') as fout:
            pickle.dump(membranes_z, fout)
