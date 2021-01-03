def age_assignment(*args,**kwargs):
    names_age = {}
    for i in args:
        names_age[i]=kwargs[i[0]]
    return names_age

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))