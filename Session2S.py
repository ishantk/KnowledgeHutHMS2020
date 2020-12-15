"""
    Built In Function on Strings
    RULE: Strings are IMMUTABLE -> They cannot Change (Any Modification will generate a new String in memory)
"""

name = "Fionna Flynn"
print("name is:", name)

upper_case_name = name.upper()

print("name now is:", name)
print("upper_case_name is:", upper_case_name)

author_name = "john watson"
cap_author_name = author_name.capitalize()
print("author_name:", author_name)
print("cap_author_name:", cap_author_name)


names = "John, Jennie, Jim, Jack, Joe"
print(names[0])
print(names[len(names)-1])

idx = names.index("h")
print("idx of h is:", idx)

idx = names.index("Jennie")
print("idx of Jennie is:", idx)

splitted_names = names.split(",")
print(splitted_names, type(splitted_names), len(splitted_names))

for name in splitted_names:
    print(name.strip())

replaced_names = names.replace('J', 'K')
print("replaced_names:", replaced_names)


quote = "Live Life King Size"
for i in range(0, len(quote)):
    print(quote[i], end=" ")

print()

for i in range(len(quote)-1, -1, -1):
    print(quote[i], end=" ")

print()

contacts = ["john", "jennie", "jack", "sia", "kim", "dave", "ana"]

search_keyword = "n"
for contact in contacts:
    # if contact.startswith("j"):
    if search_keyword in contact:
        print(contact)

song_name = "abc.mp3"
if song_name.endswith(".mp3"):
    print("We can play this audio file :)")
