Time_table={"first_period":"Numerical_Method",
            "Second_period":"Data_structure_and_algorithm",
            "Third_period":"Statistics_2nd"}
print(type(Time_table))
print(Time_table)
print(Time_table.get("Second_period"))
print(f"Your subject {(Time_table['Second_period'])}, was chaged to")
Time_table["Second_period"]="Computer_Graphics"
print(f"The changed subject is {(Time_table['Second_period'])}")
