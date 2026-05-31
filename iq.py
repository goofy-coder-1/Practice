import requests

def user_Input():
    try:
        userinput = input("Enter name of the country: ")

        return userinput
    except ValueError:
        print("wrong input")

location = user_Input()

def find_iq(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()[0]

            capital = data['capital'][0]
            population = data['population']
            region = data['region']
            return capital, population, region 
        else:
            print(f"Country not found! Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Connection Error: {e}")
        return None
    
result = find_iq(location)


if result:
    cap, pop, reg = result
    print("\n--------- COUNTRY DATA -------")
    print(f"Country:    {location.title()}")
    print(f"Capital:    {cap}")
    print(f"Region:     {reg}")
    print(f"Population: {pop:,}")
    print("--------------------------------")