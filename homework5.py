immutable_var = 19, 'Khabibulla', True
print(immutable_var)
#immutable_var.append('Denis') нельзя изменить, так как это кортеж
#print(immutable_var)
mutable_list = [19, 'Khabibulla', True]
mutable_list.append('Denis')
print(mutable_list)
mutable_list[0] = 33
print(mutable_list)
mutable_list.remove(True)
print(mutable_list)