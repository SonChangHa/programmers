import heapq

def solution(scoville, K):
    check = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        temp = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        heapq.heappush(scoville, temp + (temp2 * 2))

        if len(scoville) == 1 and scoville[0] < K:
            check = -1
            break

        check += 1

    answer = check
    return answer