#/usr/bin/python3

# Question here
#
# Create a function that counts the number of unique characters in a string
#
# Input: String
# Output: Integer

strIn = "aabb cC" #5 unique characters

def solution1(): # uses unordered set to remove duplicates
    unique = set(strIn)
    return len(unique)

def solution2(): # manually filter dupliates
    unique = []
    for char in strIn:
        if char not in unique:
            unique.append(char)
    return len(unique)

if __name__ == "__main__":
    print(solution1())
    print(solution2())
