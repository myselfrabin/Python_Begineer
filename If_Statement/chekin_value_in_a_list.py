# list=["Rabin","Roshan","Prem","Sandesh"]
# if "Hero"  in list:
#     print(list[1].upper())
# else:
#     print(type(list))   
drinks=["Vodka","Nepal ice beer","Gurkha beer","wine","whiskey"]
banned_drinks="local"
if banned_drinks not in drinks:
    print(f"{banned_drinks}, you can add this drinks too") 
drinks.append(banned_drinks)
print(f"{banned_drinks},la hai yaslai ne haliyo ava majja auncha") 
print(drinks)   
    