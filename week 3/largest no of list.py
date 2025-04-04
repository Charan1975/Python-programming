def largest_element(elements):
    return max(elements)


elements = []
limit=int(input("enter list items here : "))
for i in range(limit):
    temp=int(input("entre the elemnt : "))
    elements.append(temp)


largest_elements=largest_element(elements)
print("largest elements is",largest_elements)
