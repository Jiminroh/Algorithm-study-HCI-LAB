'''
문제 요약
- 여러 캐릭터들이 징검다리를 건넌다. 이때 최대로 넘어갈 수 있는 보폭 k가 주어질 때 최대로 건널수있는 수를 구하여라 

조건
- 징검다리는 일렬로 배치되며 디딤돌을 밟으면 숫자는 줄어든다.
- 디딤돌의 숫자가 0이되면 밟을 수 없다.
- 단, 밟을 수 있는 디딤돌이 여러개인경우 가장 가까운 디딤돌으 밟아야 한다.

'''

def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        temp = stones.copy()
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left