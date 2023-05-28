i = 0
lowest = 1000
lowestyear = ""
lowestCountry = ""

choice = 1900
average = 0

with open("life-expectancy.csv") as lifeexp_file
     for line in lifeexp_file:
         i = i + 1
         cleanLine = line.strip()
         word = cleanLine.split(",")
         if i > 1: # skip the title of the data life_file
             country = word[0]
             code = word [1]
             year = int(word[2])
             lifeexp = float(word [3])
         if lowest > lifeexp:
             lowest = lifeexp
             lowestyear = year
             lowestCountry = country
         if choiceyear == year:
             print(f"{year} - {country} - {lifeexp}")
             average = average + lifeexp
             if lowestchoice 
average = average / numChoiceYears
print(f"lowest: {lowest} - {lowestyear} - {lowestCountry}")


print("thank you very much")

