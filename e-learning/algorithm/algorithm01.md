# 1. 스택

선입후출

```python
stack = []
stack.append(5)
stack.pop()
```

# 2. 큐

선입선출

```python
from collections import deque
queue = deque()
queue.append(5)
queue.popleft()
```

# 3. 우선선위 큐(Priority Queue0

우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
|구현방법|삽입시간|삭제시간|
|---|---|---|
|리스트이용|O(1)|O(N)|
|힙(heap) |O(logN)|O(logN)|

# 4. Heap

이진 트리 자료구조의 일종  
항상 루트 노드 제거  
최소 힙 (min heap)

- 루트 노드가 가장 작은 값을 가짐
- Min-Heapify()

최대 힙 (max heap)

- 루트 노드가 가장 큰 값을 가짐
- Max-Heapify()

```python
# 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제
import sys
import heaqp
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례ㅐ로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr =[]
for i inrange(n):
    arr.append(int(input()))
res = heapsort(arr)
for i in range(n):
    print(res[i])

```

# 5. Tree

계층적인 구조  
root node: 부모가 없는 최상위 노드  
leaf node : 자식이 없는 노드  
size : 트리에 포함된 모든 노드의 개수  
depth: 루트 노드부터의 거리  
height : 깊이 중 최댓값  
degree : 각 노드의 (자식 방향)간선 개수  
트리의 크기가 N일 때, 전체 간선의 개수는 N-1

# 6. Binary Search Tree 이진 탐색 트리

왼쪽 자식 노드 < 부모 노드 < 올른쪽 자식 노드

# 7. 트리의 순회

preorder : 루트 먼저 방문 (중간-왼-오)  
inorder: 왼쪽-루트-오른쪽 (왼-중-오)  
postorder : 왼쪽-오른쪽-루트()

```python
code
```

# 8. Sorting

데이터를 특정한 기준에 따라 순서대로 나열하는 것  
**선택 정렬** - O(N\*\*2)

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[i], array[min_index] = array[min_index], array[i]
```

**삽입정렬** -O(N\*\*2)  
처리되지 않은 데이터를 하나식 골라 적절한 위치에 삽입

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array):
    for j in range(i, 0 , -1)):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1],array[j]
        else:
            break
```

**퀵 정렬** - O(NlogN)/O(N\*\*2)
기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법  
첫번째 데이터를 기준 데이터(Pivot)로 설정

```python
array = [5, 7, 9,0, 3, 1, 6, 2, 4, 8]
def quick(array, start, end):
    if start >=end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <=right):
        while(left<=end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick(array, start, right-1)
    quick(array, right+1, end)

quick(array, 0, len(array)-1)

```

**계수 정렬** - O(N+K)
데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 0, 5, 2]
count =[0]*(max(array)+1)
for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```
