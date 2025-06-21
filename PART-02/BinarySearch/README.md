## 07. 이진 탐색

### 이진 탐색이란?

이진 탐색이란, 정렬된 리스트에서 찾고자 하는 값과 중앙값을 비교하여 탐색 범위를 절반씩 효율적으로 줄여나가는 탐색 알고리즘이다.

### 이진 탐색 과정

1. 전체 범위 지정: 시작(start)은 첫 번째 인덱스 0, 끝(end)은 마지막 인덱스 9로 설정한다.
2. 중앙값 찾기: (start + end) // 2 공식을 이용해 중앙 인덱스를 계산한다.
3. 중앙값과 찾으려는 값을 비교한다.
4. 탐색 범위를 절반으로 줄인다. (중앙값보다 찾으려는 값이 더 크면, 중앙값 포함하여 중앙값보다 더 작은 값들 탐색 제외)
5. 새로운 탐색 범위에서 과정을 반복한다.

### 이진 탐색 코드 (재귀 함수 ver)

```python
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
```

### 이진 탐색 코드 (반복문 ver)

```python
def binary_seach(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

(이진 탐색은 코딩 테스트에서 단골로 나오는 문제이니 가급적 외우길 권한다고 한다.)