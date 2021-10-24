from rgb_uniform import RGBUniform

dist = RGBUniform()

for i in range(1000):
    v = dist._sample_undistorted_deterministic()
    print(v)
    x = True