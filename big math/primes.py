import numpy as np
import matplotlib.pyplot as plt

# Your existing sieve
def optimized_sieve(n):
    if n < 2:
        return []
    sieve = [True] * ((n // 2) + 1)
    sieve[0] = False
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            for j in range(i * i, n + 1, 2 * i):
                sieve[j // 2] = False
    return [2] + [2 * i + 1 for i, is_prime in enumerate(sieve) if is_prime and 2 * i + 1 <= n]

# Parameters
n = 10**5
x = np.arange(1, n+1)
prime_array = np.array(optimized_sieve(n))
pi_n = np.array([np.sum(prime_array <= i) for i in x])
approx = x / np.log(np.maximum(x, 2))

# Metrics
diff = approx - pi_n
rel_err = diff / pi_n * 100
density = pi_n / x
ratio = pi_n / approx

# Plot
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# π(n) and approximation
axs[0,0].step(x, pi_n, where='post', label=r'$\pi(n)$', color='tab:blue')
axs[0,0].plot(x, approx, 'r--', label=r'$n/\ln n$')
axs[0,0].set_title('Prime counting vs approximation')
axs[0,0].legend(); axs[0,0].grid(True, alpha=0.3)

# Absolute difference
axs[0,1].plot(x, diff, 'g')
axs[0,1].set_title('Absolute difference'); axs[0,1].grid(True, alpha=0.3)

# Relative error (%)
axs[1,0].plot(x, rel_err, 'm')
axs[1,0].set_title('Relative error (%)'); axs[1,0].grid(True, alpha=0.3)

# Prime density
axs[1,1].plot(x, density, 'c')
axs[1,1].set_title('Prime density π(n)/n'); axs[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Optional: print last‑point summary
print(f"At n={n}: π(n)={pi_n[-1]}, approx={approx[-1]:.2f}, "
      f"diff={diff[-1]:.2f}, rel_err={rel_err[-1]:.2f}%, density={density[-1]:.4f}, ratio={ratio[-1]:.4f}")
