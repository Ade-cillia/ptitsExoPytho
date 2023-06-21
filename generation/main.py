from datetime import timedelta
import time
from faker import Faker
import faker_commerce
import re
import random
import matplotlib.pyplot as plt

fake = Faker()
fake.add_provider(faker_commerce.Provider)

print("-----------1:Personal-----------")

def generate_personal():
    randomEmail = ""
    if bool(random.getrandbits(1)):
      randomEmail = fake.email()
    else:
      randomEmail = "dsbdj@dsqk@ds."
    data = {
        "username": fake.user_name(),
        "address": fake.address(),
        "email": randomEmail,
        "phone": fake.phone_number(),
    }
    return data

allPersonal = [generate_personal() for _ in range(10)]

print(allPersonal)

print("-----------2:Network-----------")

def generate_network():
    data = {
        "ip": fake.ipv4(),
        "mac_address": fake.mac_address(),
        "host": fake.hostname(),
    }
    return data

networks = [generate_network() for _ in range(10)]

print(networks)


print("-----------3:User-----------")

def generate_user():
    randomEmail = ""
    if bool(random.getrandbits(1)):
      randomEmail = fake.email()
    else:
      randomEmail = "dsbdj@dsqk@ds."
    data = {
        "name": fake.name(),
        "address": fake.address(),
        "phone": fake.phone_number(),
        "email": randomEmail,
        "password": fake.password(),
    }
    return data

users = [generate_user() for _ in range(10)]

print(users)

print("-----------4:Transaction-----------")

def generate_transaction():
    data = {
        "client_name": fake.name(),
        "iban": fake.iban(),
        "price": round(random.uniform(0, 1000), 2),
        "datetime": fake.date_time().isoformat(),
    }
    return data

allTransaction = [generate_transaction() for _ in range(10)]

print(allTransaction)

print("-----------5:Logs-----------")


def generate_log():
    data = {
        "timestamp" : int(time.time()),
        "source_ip" : fake.ipv4_public(),
        "destination_ip" : fake.ipv4(),
        "protocol" : random.choice(['TCP', 'UDP', 'ICMP']),
        "message" : "Timestamp: {timestamp} | Source IP: {source_ip} | Destination IP: {destination_ip} | Protocol: {protocol}"
    }
    return data

logs = [generate_log() for _ in range(10)]
print(logs)


print("-----------6:Telephone-----------")

def generate_telephone():
    randomEmail = ""
    if bool(random.getrandbits(1)):
      randomEmail = fake.email()
    else:
      randomEmail = "dsbdj@dsqk@ds."
    data = {
        "name": fake.name(),
        "phone": fake.phone_number(),
        "email": randomEmail,
    }
    return data

allTelephones = [generate_telephone() for _ in range(10)]

print(allTelephones)

print("-----------6:Sale-----------")

def generate_sale():
    data = {
      "clientId": fake.uuid4(),
      "product": fake.ecommerce_name(),
      "price": fake.ecommerce_price(),
      "quantity": round(random.uniform(0, 100)),
    }
    return data

allSale = [generate_sale() for _ in range(10)]

print(allSale)

print("-----------7:Students-----------")

def generate_sale():
    data = {
      "name": fake.name(),
      "age": round(random.uniform(16, 19)),
      "address": fake.address(),
      "sector": random.choice(['SSI', 'L', 'STI2D','STMG']),
    }
    return data

students = [generate_sale() for _ in range(10)]

print(students)

print("-----------8:Weather-----------")

def generate_weather():
    data = {
        "temperature": round(random.uniform(-20, 40), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "wind_speed": round(random.uniform(0, 50), 2),
        "conditions": random.choice(["Sunny", "Cloudy", "Rainy", "Snowy"]),
    }
    return data

weather_data = [generate_weather() for _ in range(10)]

print(weather_data)

print("-----------8:Hotel-----------")

def generate_hotel_reservation():
    start_date = fake.date_between(start_date='today', end_date='+30d')
    end_date = start_date + timedelta(days=random.randint(1, 7))
    
    data = {
        "client_name": fake.name(),
        "arrival_date": start_date.strftime("%Y-%m-%d"),
        "departure_date": end_date.strftime("%Y-%m-%d"),
        "num_rooms": random.randint(1, 5),
    }
    return data

hotel_reservations = [generate_hotel_reservation() for _ in range(10)]

print(hotel_reservations)
x=5
x ^= 3
print(x)
