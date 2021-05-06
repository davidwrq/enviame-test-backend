from faker import Faker  
from app.models import Enterprise

for i in range(50):
    fake = Faker() 
    name = fake.company()

    enterprise = Enterprise(name=name)
    enterprise.save()