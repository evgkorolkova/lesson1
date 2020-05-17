#1
city_temperature = {
"city": "Москва",
"temperature": 20
}
print(city_temperature["city"])
city_temperature["temperature"] -= 5
print(city_temperature)

#2
print(city_temperature.get("country"))
city_temperature.get("country", "Россия")
city_temperature["date"] = "27.05.2019"
print(len(city_temperature))
