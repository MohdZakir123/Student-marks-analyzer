numbers = input("Number of students: ")
marks = list(map(int, input("Enter the marks: ").split()))

print("Highest marks: ", max(marks))
print("Lowest marks: ", min(marks))
print("Average marks: ", sum(marks)/int(numbers))
print("Total marks: ", sum(marks))
print("pass percentage: ", (len([m for m in marks if m>=35])/int(numbers))*100)
print("Fail percentage: ", (len([m for m in marks if m<35])/int(numbers))*100)