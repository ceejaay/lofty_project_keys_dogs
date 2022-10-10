import requests
import random
import time
from faker import Faker

fake = Faker()

# post
NEW_KEY = "http://localhost:8000/keys/"
# get
ALL_KEYS = "http://localhost:8000/keys/"

# get
ONE_KEY = f"http://localhose:8000/keys/key_detail/{random.randint(1, 200)}"
# put
UPDATE_KEY = f"http://localhose:8000/keys/key_detail/{random.randint(1, 200)}"


create_data = {
        'key': fake.word(),
        'value': random.randint(1, 1000)
        }

req = requests.get(ALL_KEYS)
print(req)

for req in range(1, 50):
    req = requests.post(ALL_KEYS, data=create_data)
    time.sleep(2)
    print(req.headers)
