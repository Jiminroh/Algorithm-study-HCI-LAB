'''
<문제요약>
공백으로 구분된 숫자들이 입력될 때 (최댓값) (최솟값)형태로 나타내어라 
'''

def solution(s):
    li = list(map(int, s.split(' ')))
    return str(min(li)) + " " + str(max(li))