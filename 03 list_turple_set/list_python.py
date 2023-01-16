l = ['Bob', 'Makafui']

t = ('a', 'b', 'c')

s = {'bb', 'yy', 'dd'}#This has no order
ss = {'bb', 'yy', 'hh'}



# ======================
s.remove('bb')
s.add('kenn')
# ======================

# ====================
result = s.union(ss)
print(result)
# ======================


# ====================
both = s.intersection(ss)
print(both)


# print(dir(s))