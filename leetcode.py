# 118. Pascal's Triangle

def pascalsTriangle(numRows) -> list:
    pascal=[[1]]
    for i in range(1, numRows):
        curr = [1]
        for j in range(1, i):
            curr.append(prev[j]+prev[j-1])
        curr.append(1)
        pascal.append(curr)
        prev=curr
    return pascal

print(pascalsTriangle(5))
print(pascalsTriangle(1))
