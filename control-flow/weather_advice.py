weather = input("What's the weather like today? (sunny/rainy/cold):").lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "cold":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "rainy":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
