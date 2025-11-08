age = 47
name = "Vova"
is_validation = age > 0 and age <= 130
print(is_validation)
print(age in range(1, 34)) # Верхняя граница не включается.
age = 33
print(age in range(1, 34))