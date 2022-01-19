import argparse
from numpy import *
import matplotlib.pyplot as plt

# - - Command line arguments - -

parser = argparse.ArgumentParser(
    description='Plot the superposition of two waves by definition of '
                'frequencies, amplitude and time',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)


def add_parser_argument(short_flag, full_flag, description, default_value):
    parser.add_argument(
        short_flag, full_flag, metavar='', type=float,
        default=default_value, required=False, help=description
    )


add_parser_argument('-w1', '--wave1', 'wave 1 frequency (Hz)', 30)
add_parser_argument('-w2', '--wave2', 'wave 2 frequency (Hz)', 32)
add_parser_argument('-a', '--amplitude', 'waves amplitude (m)', 10)
add_parser_argument('-t', '--time', 'points to evaluate function (s)', 2)
args = parser.parse_args()

# - - Sine wave modeling - -


def eval_sine_wave(amplitude, angular_frequency, time):
    # evaluates y = Asin(-ωt)
    return amplitude * sin(angular_frequency * time)


def get_angular_frequency(frequency):
    # evaluates ω = 2πf
    return (2 * pi) * frequency


f1, f2 = args.wave1, args.wave2  # wave frequencies in Hz
time_points = arange(0, args.time, 0.001)  # points to evaluate function
wave1 = eval_sine_wave(args.amplitude, get_angular_frequency(f1), time_points)
wave2 = eval_sine_wave(args.amplitude, get_angular_frequency(f2), time_points)

# - - Wave plotting - -

fig, axs = plt.subplots(
    4, sharex='all', figsize=(12, 7),
    gridspec_kw={'height_ratios': [2, 2, 2, 4]}
)

# title, subtitle, axis labels
fig.suptitle(
    'Demonstration of beat patterns as a product of wave interference',
    size=14
)
fig.text(0.5, 0.025, 'Time (ms)', ha='center')
fig.text(0.008, 0.54, 'Amplitude (m)', va='center', rotation='vertical')
fig.text(
    0.5, 0.92, 'A beat pattern is produced by the superposition of two waves '
    'of slightly different frequencies', ha='center''', size=9
)
fig.tight_layout(pad=2.8)

# subplot - wave 1
axs[0].plot(wave1, color='#e23654')
axs[0].set_title(
    f'f1 = {f1:.2f} Hz; ω1 = {get_angular_frequency(f1):.2f} rad/s',
    loc='left', size=11
)

# subplot - wave 2
axs[1].plot(wave2, color='#627ddb')
axs[1].set_title(
    f'f2 = {f2:.2f} Hz; ω2 = {get_angular_frequency(f2):.2f} rad/s ',
    loc='left', size=11
)

# subplot - wave superposition
axs[2].plot(wave1, color='#e23654')
axs[2].plot(wave2, color='#627ddb')
axs[2].set_title('Superposition (f1+f2)', loc='left', size=11)

# subplot - resultant pattern
axs[3].plot(wave1+wave2, color='#635e9d')
axs[3].set_title(
    f'Resultant beat pattern (fb = {abs(f1-f2):.2f} Hz; '
    f'ωb = {get_angular_frequency(abs(f1-f2)):.2f} rad/s)',
    loc='left', size=11
)

for ax in axs:
    ax.yaxis.set_major_formatter(lambda tick, position: str(abs(tick)))
    ax.grid()

plt.savefig('beat_pattern.png')
plt.show()
