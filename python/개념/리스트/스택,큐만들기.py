#리스트에서 pop()로하면 스택구조임
#리스트에서 pop(0)하면 큐 구조임

#데큐도 할수있다
from collections import deque
a=deque([10,20,30])
a.append(50)    #덱의 오른쪽에 추가
a.popleft()     #덱의 왼쪽 요소 하나 삭제
print(a)