'''
문제 : 프로그래머스 2022 KAKAO TECH INTERNSHIP 두 큐 합 같게 만들기 

<문제 요약>
1. 길이가 같은 두 개의 큐가 주어짐 
2. pop, insert를 이용하여 두 배열의 원소의 합이 같게 만들어라.

pop -> 배열의 앞에있는 원소추출 
insert -> 배열의 끝에 원소추가 
1번의 pop & 1번의 insert는 1회

단, 같게 만들 수 없을 경우 return -1
'''
from collections import deque

def solution(queue1, queue2):
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    sum_1 = sum(deq1)
    sum_2 = sum(deq2)

    for i in range(len(queue1) * 4): # 반복횟수 정하기 
        if sum_1 == sum_2: # 두 큐의 합이 같다면 return 
            return i
        if sum_1 > sum_2: # queue1의 합이 큰 경우 
            tmp = deq1.popleft()
            deq2.append(tmp)
            sum_1 -= tmp
            sum_2 += tmp
        else:
            tmp = deq2.popleft() # queue2의 합이 큰 경우 
            deq1.append(tmp)
            sum_2 -= tmp
            sum_1 += tmp
    return -1
