def sort(arr):
  left = 0
  right = len(arr) -1

  while left <right and arr[left] <=arr[left +1]:
    left +=1
  if left == right:
    return 0
  while right >0 and arr[right] >= arr[right-1]:
    right -=1

  arrmin = -float('inf')
  arrmax = float('inf')
  for i in range(left,right):
    arrmax = max(arrmax,arr[i])
    arrmin = min(arrmin,arr[i])

  while left < arrmin:
    left -=1
  while right > arrmax:
    right+=1
  return right-left+1

if __name__ == '__main__':
  array = [1, 2, 5, 3, 7, 10, 9, 12]
  ans = sort(array)
  print(ans)