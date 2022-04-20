n = int(input())
m_number = 0
for i in range(1,n+1):
    div_number = sum(map(int,str(i)))
    m_number = i + div_number
    if(m_number == n):
        m_number = i
        break

    if i == n:
        m_number = 0
print(m_number)