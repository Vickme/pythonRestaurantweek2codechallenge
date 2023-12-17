from lib.customer import Customer
from lib.restaurant import Restaurant 
from lib.review import Review 

customer1 = Customer("victor", "Njutha")
customer2 = Customer("Cedric", "Njutha")

restaurant1 = Restaurant("KFC")
restaurant2 = Restaurant("Pizzahut")

review1 = Review(customer1, restaurant1, 10)
review2 = Review(customer2, restaurant2, 6)

print(f"Name :  {customer1.full_name()}")
print(f"Rating : {restaurant2.average_star_rating()}")
print(f"Review : {customer2.num_reviews()}")