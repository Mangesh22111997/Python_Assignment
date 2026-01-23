"""
Question: Write a program which accepts one character and checks whether it is vowel or consonant.
Input: a
Output: Vowel

"""

def isVowel(character):
        
    if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
        return True
    return False

def main():
    characterToPass = str(input("Enter Single Character: "))
    if isVowel(characterToPass):
         print("Vowel")
    else:
         print("Not a Vowel")

if __name__ == "__main__":
    main()