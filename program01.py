student=[[11,'dev',99,98],[61,'suri',88,80],[16,'hari',74,64],[22,'jeevna',91,92]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
