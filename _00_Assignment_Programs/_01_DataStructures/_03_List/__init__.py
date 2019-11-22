'''''
basic list data
'''''
emp_ids1 = [123, 323, 56, 456]
print(emp_ids1)
emp_ids1.append(890)                # Appending element to last index
print(emp_ids1)
emp_ids1.insert(3, 100)             # Inserting element at index 3
print(emp_ids1)
del emp_ids1[2]                     # Deleting element at index 2
print(emp_ids1)
print(emp_ids1[4])
emp_ids2 = [111, 123, 123, 453, 768]
emp_ids = emp_ids1 + emp_ids2       # Adding two lists
print(emp_ids)
print(len(emp_ids))                 # Finding length of the list
