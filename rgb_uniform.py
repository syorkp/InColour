from scipy.stats import uniform
import numpy as np

# Space transformations:
# Apply linear transform with np.dot()
# Nonlinear transform?
# Could just apply scaling to one or other dimension, followed by normalisation. E.g. r = r^2.3, which can be updated.
# Or, can express each dimension as something like a sigmoid function - like Richard was doing, with updates to it
# moving parameters that cause squashing of space. Also, make sure when scaling, shifts the other two dimensions.
# TODO: Determine a suitable equation to apply to each, which has parameters which can be updated.

# Sampling:
# If using non-repeating sampling, should use previous samples to create PDF that determines acceptance of a sample.
# Can also have another PDF that is input, or can be uniform, and these together determine acceptance p.


class RGBUniform:

    def __init__(self, normalise=False, total_samples=1000):
        self.normalise = normalise
        self.vector_space_transform = None
        self.sample_index = 0

        self.total_samples = total_samples
        self.samples_per_dim = np.around(total_samples ** (1/3))
        self.dimension_interval = 1/self.samples_per_dim
        self.dimension_decimals = 1

    def _sample_undistorted(self):
        r = uniform.rvs()
        g = uniform.rvs()
        b = uniform.rvs()
        self.sample_index += 1
        return [r, g, b]

    def _sample_undistorted_deterministic(self):
        r_index = self.sample_index % self.samples_per_dim
        g_index = (self.sample_index // self.samples_per_dim) % self.samples_per_dim
        b_index = (self.sample_index // self.samples_per_dim ** 2) % self.samples_per_dim
        if self.sample_index < self.total_samples:
            self.sample_index += 1
        rgb = [r_index, g_index, b_index]
        rgb = [np.around(i * self.dimension_interval, self.dimension_decimals) for i in rgb]
        return rgb

    def sample(self):
        """Based on previous samples, and distribution density, returns a 3D vector of RGB values."""

    def update_model(self, rgb_vector, success):
        """Uses a correct/incorrect guess to update the transform of vector space"""

    def transform_rgb(self):
        """Based on current distortions of space, returns the analogue of a 3D RGB vector"""


# Make samples dependent on density - np.uniform with density value for acceptance, and on previous guesses by
# creaiting distribution of previous guesses. Requires tuning.
