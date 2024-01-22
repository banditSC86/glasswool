import numpy as np
import numba

@numba.njit
def remove_outliers(data, n_std=3):
  """
  Iteratively removes non-Gaussian outliers from a list of numbers until no more outliers are found,
  using iterative updates of mean and standard deviation for efficiency. Optimized with Numba.

  Args:
    data: A list of numbers.
    n_std: The number of standard deviations to consider as an outlier.

  Returns:
    A list of numbers without outliers.
  """

  filtered_data = data  # Use the same array for efficiency
  n = len(filtered_data)

  while True:
    original_length = n
    mean = 0.0
    std = 0.0

    # Iteratively calculate mean and standard deviation (Numba-optimized)
    for i in range(n):
      x = filtered_data[i]
      mean += x
      std += x**2

    mean /= n
    std = np.sqrt(std / n - mean**2)  # Corrected std calculation for Numba

    # Iteratively update mean and standard deviation for removed outlier
    i = n - 1
    while i >= 0:
      x = filtered_data[i]
      if abs(x - mean) > n_std * std:
        # Update mean and standard deviation efficiently
        mean -= (x - mean) / n
        std = np.sqrt(((n - 1) * std**2 - (x - mean)**2) / (n - 2))
        filtered_data[i] = filtered_data[n - 1]  # Swap with the last element
        n -= 1
      i -= 1

    if n == original_length:
      break  # No more outliers found, exit the loop

  return filtered_data[:n]  # Return the filtered portion of the array
