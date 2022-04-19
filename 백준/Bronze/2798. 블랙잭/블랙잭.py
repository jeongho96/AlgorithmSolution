# 블랙잭 2798번
def black_jack(n,m,list1):
    answer = 0
    for i in range(0, len(list1)):
        for j in range(i + 1, len(list1)):
            for k in range(j + 1, len(list1)):
                sum1 = list1[i] + list1[j] + list1[k]
                if sum1 <= m:
                    answer = max(answer,sum1)           
        
    return answer


n,m = map(int,input().split())
list1 = list(map(int,input().split()))
print(black_jack(n,m,list1))
