"""Mencari nilai profit terbesar dengan membandingkan antara profit hari ini dengan profit sebelumnya
tetapi jika tidak ada profit sama sekali pada data yang tersedia, akan mengambalikan nilai -1

Contoh :

Input : 10, 12, 4, 5, 9
Output : 5
"""

def profit_max(arr):
  sell = 0
  max_profit = 0

  get_array = arr[0]
  for i in range(len((arr))):
      get_array = min(get_array, arr[i])
      sell = arr[i] - get_array
      if not max(max_profit, sell):
        max_profit = -1
      else :
        max_profit = max(max_profit, sell)
        
  
  arr = max_profit
  return arr


arr = [10,12,4,5,9]
print ArrayChallenge(profit_max(arr))
