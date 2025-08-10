## 10. 그래프 이론

### 서로소 집합

수학에서 **서로소 집합**이란 **공통 원소가 없는 두 집합**을 의미한다. 서로소 집합 자료구조는 몇몇 그래프 알고리즘에서 매우 중요하게 사용된다. 서로소 집합 자료구조는 union과 find 이 2개의 연산으로 조작할 수 있다.

1. **Find (찾기)**: 특정 원소가 어떤 그룹(집합)에 속해 있는지 확인한다.
2. **Union (합치기)**: 두 개의 그룹(집합)을 하나의 그룹으로 합친다.

서로소 집합은 보통 **트리** 자료 구조를 이용해 구현한다. 핵심 개념은 각 그룹(집합)마다 **'대표 원소'**를 하나씩 정하는 것이다. 같은 그룹에 속한 모든 원소는 이 동일한 대표 원소를 가리키게 된다.
- **Find(x) 연산**: 원소 x가 속한 그룹의 '대표 원소'가 누구인지 찾아 반환한다.
- **두 원소의 소속 확인**: Find(A)와 Find(B)의 결과(대표 원소)가 같다면, A와 B는 같은 그룹이다. 다르다면 다른 그룹이다.
- **Union(A, B) 연산**: A가 속한 그룹과 B가 속한 그룹을 합친다. 한쪽 그룹의 대표 원소가 다른쪽 그룹의 대표 원소를 가리키도록 만들어 하나의 그룹을 만든다. (보통 번호가 더 작은 원소가 부모 노드가 되도록 구현한다.)

#### 구현 방식 (트리 구조)

- **배열**: parent 라는 배열을 만든다. parent[i] 는 i번 원소의 부모 노드를 저장한다.
- **대표 원소**: 만약 parent[i] == i라면, i는 그 그룹의 대표 원소(루트 노드)이다.

**초기 상태**: 모든 원소는 자기 자신만을 포함하는 별개의 그룹으로 시작한다. 따라서 모든 원소의 부모는 자기 자신이다.

**진행**: 모든 union(합집합) 연산을 처리한다. (이 때, union 연산 구현을 위해 find 연산이 필요하다.)

#### 기본적인 서로소 집합 알고리즘 소스코드

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
```

#### 경로 압축 기법

위의 방식대로만 구현하면 트리가 한쪽으로 길게 늘어지는 **편향 트리**가 될 수 있다. 이 경우 Find 연산이 모든 노드를 다 거쳐야 하므로 비효율적이다. 이를 방지하기 위해 여러 최적화 기법 중 경로 압축 기법을 적용해볼 것이다.

경로 압축 기법은 **find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신**하는 기법이다.

기존 코드에서 find 함수를 다음과 같이 변경하면 경로 압축 기법의 구현이 완료된다.

```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```