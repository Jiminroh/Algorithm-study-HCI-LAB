'''
문제 요약 
- 사용자 아이디와 제제 아이디가 주어졌을 때 나올수 있는 경우의 수를 구하여라
'''

from itertools import permutations
    
def check(user, ban):
    if len(user) != len(ban):
        return False
    else:
        for i, j in zip(user, ban):
            if j == '*':
                continue
            if i != j:
                return False
        return True
        
def solution(user_id, banned_id):
    answer = []
    
    for i in permutations(user_id, len(banned_id)):
        count = 0
        for a, b in zip(i, banned_id):
            if check(a, b):
                count += 1
                
        if count == len(banned_id):
            if set(i) not in answer:
                answer.append(set(i))
    
    return len(answer)



        