names = input('Enter your name: ').split(",")
assignments = input('Enter the name of the assignment: ').split(",")
grades = input("Enter your grade: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, asn, grds in zip(names, assignments, grades):
    print(message.format(name, asn, grds, int(grds) + int(asn) * 2))