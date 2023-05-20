

cache = dict()
result = []
triangle = []


# Computes Pascal Triangle by using Recursive approach
def recursive( row ):
            
    if row in cache.keys():
        return cache[row]

    if row == 0:
        cache[row] = [1]
        return [1]
        
    else:
        line = []
        prev = recursive( row - 1 )
        for i in range( row ):
            if i == 0:
                line.append(1)
            else:
                line.append( prev[i-1] + prev[i] )
            
        line.append(1)

        cache[row] = line
        return line

    


# Computes Pascal Triangle by using Iterative approach
def iterative( rows ):
    
    for i in range( rows ):
        result.append([])
         
        for j in range( i ):
            if j == 0:
                result[i].append(1)
            else:
                result[i].append( result[i - 1][j-1] + result[i - 1][j])
        
        result[i].append(1)


if __name__ == '__main__':
    rows = int(input("Enter no. of rows : "))

    iterative(rows)
    
    for i in range(rows ):
        triangle.append(recursive( i ))

    print("Pascal Triangle Using Iteration.....!")
    for x in result:
        print( "  " * (rows - len(x)), end='')
        print(*x, sep='   ')
    
    print("\n\nPascal Triangle Using Recursion.....!")
    for x in triangle:
        print( "  " * (rows - len(x)), end='')
        print(*x, sep='   ')