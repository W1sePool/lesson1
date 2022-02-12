from itertools import product


product = {
"city" : "Москва",
"temperature" : 20
}
print(product["city"])
product["temperature"] = product["temperature"] - 5
print(product.get("country","нет такого ключа"))
product["country"] = "Россия"
print(product.get("country","Россия"))
product["date"]="27.05.2019"
print(product)
print(len(product))

