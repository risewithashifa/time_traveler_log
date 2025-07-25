import datetime
current_year = datetime.datetime.now().year
travel_log={}
print("Welcome to the Time Traveler's Log...")
while True:
 year = int(input("Enter the year you want to travel to:"))
 if year<current_year:
    print(f"you have traveled {current_year-year} years into the past!")
 elif year>current_year:
    print(f"you have traveled {year-current_year} years into the future!")
 else:
    print(f"you are in present! The year is {year}")
 note = input("What would you like to note for this year?")
 travel_log[year] = note
 choice = input("Do you want to travel to another year? (yes/no):").lower()
 if choice!="yes":
     break
print("\n Your time Travel log:")
for year,note in travel_log.items():
    print(f"{year}: {note}")
print("\n Thank You for Travelling through time with us! ")

