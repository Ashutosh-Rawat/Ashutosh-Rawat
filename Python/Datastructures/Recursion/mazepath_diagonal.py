def getDiagonalPath(currentRow, currentColumn, finalRow, finalColumn):
    if currentRow == finalRow and currentColumn == finalColumn:
        list = []
        list.append('')
        return list
    if currentRow > finalRow or currentColumn > finalColumn:
        return None
    finalResult = []
    result = getDiagonalPath(currentRow+1, currentColumn+1, finalRow, finalColumn)
    for r in result:
        finalResult.append(' H-V '+r)
    return finalResult

#testing
result = getDiagonalPath(0,0,4,4)
print(result)


result = getDiagonalPath(0,0,5,5)
print(result)
