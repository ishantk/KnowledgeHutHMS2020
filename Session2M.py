# Sets
# followers = ["john.w", "fionna", "dave.h", "fionna", "kia", "ana", "ana"]
# followers = ("john.w", "fionna", "dave.h", "fionna", "kia", "ana", "ana")
followers = {"john.w", "fionna", "dave.h", "fionna", "kia", "ana", "ana"}
print(len(followers))

# ASCII Code Based :)
print(min(followers))   # ana
print(max(followers))   # kia

# Sets will store data using Hashing and Hence Data will be UnOrdered and Unique :)
print("followers:", followers)

for follower in followers:
    print(follower)

