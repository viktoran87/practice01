immutable_var=tuple=1, 2, 3, 'A', 'B', 'C'
print(immutable_var)
# tuple[1]=33
print(tuple) # кортежи используются для хранения списков, которые должны оставаться неизменными, поэтому кортеж не поддерживает обращение по элементам.
mutable_list=[1, 2, 3, 'a', 'b', 'c']
print(mutable_list)
mutable_list[3]='i'
print(mutable_list)