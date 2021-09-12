def solution(participant, completion):
    answer = ""
    dic1 = {}
    dic2 = {}
    
    for i in participant:
        if i not in dic1:
            dic1[i] = 1
        else:
            dic1[i] += 1
            
    for i in completion:
        if dic1[i] > 1:
            dic1[i] -= 1
        else:
            del dic1[i]

    for i in dic1:
        answer += i
    return answer
