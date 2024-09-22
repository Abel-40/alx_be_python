weather_status = input("what's the weather like today? (sunny/rainy/cold):")
if weather_status == "sunny":
  print('Wear a t-shirt and sunglasses.')
elif weather_status == "rainy":
  print("Don't forget your umbrella and a raincoat.")
elif weather_status == "cold":
  print("Make sure to wear a warm coat and a scarf.")
else :
  print("Sorry, I don't have recommendations for this weather.")
