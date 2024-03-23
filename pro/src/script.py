from detector import predict

username = input("Enter the Username to verify: ")

values = []
for i in range(14):
    value = input(f"Enter value {i+1}: ")
    values.append(value)

print(predict(username, values))
