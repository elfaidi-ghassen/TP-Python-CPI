# Q1
car_1 = dict(trade="Renault", model="Golf", code="102TN155", color="Red", power=7)
car_2 = dict(trade="Volkswagen", model="Clio", code="506TN201", color="Black", power=4)
car_3 = dict(trade="Peugeot", model="Golf", code="8002TN", color="White", power=6)
car_4 = dict(trade="Volkswagen", model="Polo", code="4000TN122", color="Gray", power=5)

# Q2
cars = [car_1, car_2, car_3, car_4]

# Q3
for car in cars:
    if car["power"] >= 5:
        print(f"{car['model']} ({car['trade']}): {car['power']}")

# Q4
while True:
    prompt = input("Type a trade: ")
    if prompt in [car["trade"] for car in cars]:
        print(f"List of cars having the trade {prompt}:")
        list_of_cars = [car for car in cars if car["trade"] == prompt]
        for c in list_of_cars:
            print(c)
        break
    print("trade doesn't exist!")
    
# Q5
print("####")
for car in cars:
    if car["color"] == "Red":
        car["color"] = "Green"
