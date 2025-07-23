def detect_anomalies(arr, tolerance, index=0, anomalies=None):
  """
  Takes a list of values and records a rolling average, if it detects an anomalous value which is different to the rolling value by the given margin its index gets added to a list which gets returned.

  Args:
    arr (list): List of numbers greater than length 3
    tolerance (float): Represents how different a value can be from the rolling average.
  """
  
  if anomalies is None:
    anomalies = []
  
  # Base case where we reach the end of the list because we're comparing 3 at at time.
  if index + 3 >= len(arr):
    return anomalies
  
  # Sums up index, index + 1, index + 2 and averages it
  average = sum(arr[index: index+3])/3

  # Index + 3 because we're comparing the next value to the previous 3
  if abs(average - arr[index + 3]) > tolerance:
    anomalies.append(index + 3)
  
  return detect_anomalies(arr, tolerance, index+1, anomalies)