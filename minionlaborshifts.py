def solution(data, n):
  return[x for x in data if data.count(x)<=n]

print('Test case 1:',solution([1,2,3],0))
print('Test case 2:',solution([1,2,2,3,3,3,4,5,5],1))
print('Test case 3:',solution([5,10,15,10,17],1))
