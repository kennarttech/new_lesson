result = list(range(8))
print(result)

empty = []
for i in result:
    empty.append(result)
    print(empty)


print()
if len(empty) >= 2:
    print('the empty contains more items')
else:
    print('less than that')




gh = ['a', 'b', 'c']
for i in enumerate(gh):
    print(i[1], i)

print()
print(result[::-1])