from mpmath import mp
import time

def compute_pi_mpmath(digits):
    mp.dps = digits  # set decimal places
    return str(mp.pi)

# ⏱ Benchmark
start = time.time()
pi_val = compute_pi_mpmath(100)
end = time.time()

print(f"π to 100 digits:\n{pi_val}")
print(f"⏱ Computation Time: {end - start:.4f} seconds")