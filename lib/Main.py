from Customer import Customer
from Restaurant import Restaurant 
from Review import Review 

Customer1 = Customer("victor", "Njutha")
Customer2 = Customer("Cedric", "Njutha")

Restaurant1 = Restaurant("KFC")
Restaurant2 = Restaurant("Pizzahut")

Review1 = Review(Customer1, Restaurant1, 10)
Review2 = Review(Customer2, Restaurant2, 6)

print(f"Name :  {Customer1.full_name()}")
print(f"Rating : {Restaurant2.average_star_rating()}")
print(f"Review : {Customer2.num_reviews()}")