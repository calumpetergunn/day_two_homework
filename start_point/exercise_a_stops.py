stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]


#1. Add "Edinburgh Waverley" to the end of the liststops.append("Edinburgh Waverley")
stops.append("Edinburgh Waverley")
#correct

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
#correct

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")
#correct

#4. Print out the index position of "Linlithgow"
print(stops.index("Linlithgow"))
#correct

#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
#correct

#6. Delete "Cumbernauld" from the list by index
stops.pop(2)
# or stops.pop(stops.index("Cumbernauld")) #
# Alternatively use the del operator
# del stops[stops.index("Cumbernauld")]

#7. Print the number of stops there are in the list
num_stops = len(stops)
print(num_stops)
#sure why not

#8. Sort the list alphabetically
stops = sorted(stops)
# stops.sort()

#9. Reverse the positions of the stops in the list
stops.reverse()
#correct

#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)
# bing bang boom
