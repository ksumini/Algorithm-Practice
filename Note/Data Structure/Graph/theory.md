# 그래프
![image](https://github.com/ksumini/Algorithm-Practice/assets/70088803/7e0c9700-52d4-4452-9de6-fbf3b57335f9)
- 여러 개의 객체(노드 또는 정점)와 이들 사이의 연결(엣지 또는 간선)로 구성된 자료구조
</br>

## 그래프 관련 용어
![image](https://github.com/ksumini/Algorithm-Practice/assets/70088803/2be2642d-8006-4f87-8aa0-38be33ed289d)
- **정점**(Node, Vertex)
- **간선**(Edge): 정점간의 관계
- **G = (V, E)** 로 나타낸다.
![image](https://github.com/ksumini/Algorithm-Practice/assets/70088803/1fdcae0f-8140-49da-9a05-cbf291d01111)
- **경로**: 정점 A에서 B로 가는 경로
  - A -> B
  - A -> C -> D -> E -> B 

- **사이클**: 정점 A에서 다시 A로 돌아오는 경로 (시작 정점 = 도착 정점)
  - A -> C -> B -> A
  - A -> C -> E -> B -> A
- **차수**: 정점과 연결된 간선의 개수로 방향 그래프의 경우에는 진입차수(In-degree), 진출차수(Out-degree)로 나누어서 차수를 계산한다.
  - **진입차수(In-degree)**: 방향 그래프에서 외부에서 오는 간선의 수
  - **진출차수(Out-degree)**: 방향 그래프에서 외부로 향하는 간선의 수
  - 그림에서 E의 In-degree: 2, Out-degree: 1

 </br>
 
## 그래프의 종류
![image](https://github.com/ksumini/Algorithm-Practice/assets/70088803/8c6e9df3-8f18-4a44-8dcc-c2a1500f35e0)
### 무방향(=양방향) 그래프(Undirected Graph)
- 방향이 없는 그래프
- 간선을 통해, 노드는 양방향으로 갈 수 있음
### 방향 그래프(Directed Graph)
- 간선에 방향이 있는 그래프 
### 가중치 그래프(Weighted Graph) 또는 네트워크(Network)
- 간선에 비용 또는 가중치가 할당된 그래프
### 순환 그래프(Cyclic Graph)
- 순환 그래프는 하나 이상의 사이클(cycle)을 포함하는 그래프
- 즉, 어떤 정점에서 출발하여 여러 정점을 거쳐 다시 그 정점으로 돌아오는 경로가 존재하는 그래프
### 비순환 그래프(Acyclic Graph)
- 사이클이 전혀 존재하지 않는 그래프
- 즉, 어떤 정점에서 출발하여 여러 정점을 거쳐 다시 그 정점으로 돌아오는 경로가 존재하지 않는 그래프
</br>
 
## 그래프의 표현
### 인접 행렬
![image](https://github.com/ksumini/Algorithm-Practice/assets/70088803/aa1639b7-0fbd-4c21-a6c5-1027c69dd12b)
- 정점의 개수를 V라고 할 때, V X V 크기의 이차원 배열을 이용한다.
- A[i][j] = 1(i -> j 간선이 있을 때), 0(없을 때) -> 정점이 V개이고 간선이 E개일 때 어떤 두 점이 연결되어 있는지를 O(1)에 알 수 있다는 장점
- 공간복잡도: O(V^2)
```python
v = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))

# Directed Graph (방향 그래프)
adj_matrix = [[0]*v for _ in range(v)]
for _ in range(e):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1


# Undirected Graph (무방향 그래프)
adj_matrix = [[0]*v for _ in range(v)]
for _ in range(e):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1
```

### 인접 리스트
![image](https://github.com/ksumini/Algorithm-Practice/assets/70088803/bb1ae520-e0f1-4138-99c1-abe158629bdc)
- 리스트를 이용해서 구현
- A[i] = i와 연결된 정점을 리스트로 포함
- 링크드 리스트나 길이를 동적으로 변경할 수 있는 배열을 사용한다
- 인접 행렬과 비교했을 때 정점이 많고 간선은 상대적으로 작은 상황에서 공간을 절약할 수 있는 방식
- 공간복잡도: O(V+E)
```python
v = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))

# Directed Graph (방향 그래프)
adj = [[] for _ in range(v)]
for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)


# Undirected Graph (무방향 그래프)
adj = [[] for _ in range(v)]
for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
```

