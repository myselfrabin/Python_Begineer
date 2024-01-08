capitals={"Nepal":"kathmandu",
        "India":"New Delhi",
         "USA":"Washington D.C",
          "Russia":"Moscow",
           "China":"Beijing"}
print(capitals['Nepal'])
print(capitals.get("Nepal"))
print(capitals["India"])
print(capitals.get("India"))
print(capitals["USA"])
print(capitals.get("USA"))
print(capitals["Russia"])
print(capitals.get("Russia"))
print(capitals["China"])
print(capitals.get("China"))
print(capitals.get("Hello"))
capitals.update({"Japan":"Tokyo"}) #using this update()we can insert a key-value in a dictionary
print(capitals)