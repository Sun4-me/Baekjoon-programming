# Py-Algorithms
:green_book: Python implementations of algorithms and data structures. 

---

# Baekjoon
꾸준한 알고리즘 연습 일기장
- Since 2022.12.29 ~
- 나의 백준 현황 : [ 백준(sun4_me) ](https://www.acmicpc.net/user/sun4_me)
- `Python3`


#### 목표
- **매일** 최소 두 문제 이상 풀기
- 도저히 방법을 모를 때 까지 스스로 풀기
- 맞춘 문제도 간소화, 다른 풀이 방법 고민하기
- 8월까지 티어 골드 달성

---

# Tip
## 시간 초과 / 입출력 속도 개선하기

- input()
  ```py
  word = input(" 단어 입력 : ")
  ```
  Promt message를 파라미터로 받으며, 개행문자(enter)가 입력 되면 버퍼의 입력이 종료 되는 것으로 간주
  
- sys.stdin.readline()
  ```py
  word = sys.stdin.readline()
  ```
  Promt message를 파라미터로 받지 않으며, 개행문자를 포함하여 한번에 읽어와 버퍼에 보관함( 사용자 요구시 읽어올 수 있음 )
  
**Baekjoon 에서는 입력값에 promt message가 필요가 없다. 따라서 시간 초과 오류가 났을때 sys입력방식으로 바꾸면 정답으로 바뀔 가능성이 높다.**
```py
import sys
tmp = sys.stdin.readline()
```

> 공부하기 좋은 코드 

- [2751 수 정렬하기 2.py](https://github.com/Sun4-me/Baekjoon/blob/d90007e2c219a6a73068d6b334f77e691af85001/Silver/2751%20%EC%88%98%20%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B02.py)
- [1225 이상한 곱셈.py](https://github.com/Sun4-me/Baekjoon/blob/d90007e2c219a6a73068d6b334f77e691af85001/Bronze/1225%20%EC%9D%B4%EC%83%81%ED%95%9C%20%EA%B3%B1%EC%85%88.py)

## 메모리 초과

- List Comprehension 사용하기

```py
## for loop
## for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용못한다.
num_list = []
for i in range(10000):
	num_list.append(i)
    
## List comprehension
num_list = [i for i in range(10000)]
```

**입력값이 극한으로 주어질 때는 메모리를 효율적으로 관리해주기 위해 `num_list = [0] * 10001` 처럼 리스트를 미리 만들어두거나, List comprehension을 사용하면 메모리 초과 오류를 해결할 가능성이 높다.**

> 공부하기 좋은 코드 

- [10989 수 정렬하기 3.py ](https://github.com/Sun4-me/Baekjoon/blob/d90007e2c219a6a73068d6b334f77e691af85001/Bronze/10989%20%EC%88%98%20%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%203.py)
