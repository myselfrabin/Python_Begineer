# alien={'color':'green','points':5}
# new_point=alien['points']
# print(f"The point you get is={new_point}")
# print(alien['color'])
# print(alien['points'])

alien={'color':'green','points':5}
print(alien)
alien={'color':'green','points':5,'y_position':25,'x_position':0}
print(alien)
# print(help(alien))
print(alien.get("rabin"))
if alien.get("rabin"):
    print("The color exist")
else:
    print("The color doesnot exist")    