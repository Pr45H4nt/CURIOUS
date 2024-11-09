import random
alphabet = list("abcdefghiklmnopqrstuvwxyz ")

def character(word):
    r = None
    c = 0
    while r != word:
        r = "".join(random.choices(alphabet,k=len(word)))
        print(r)
        c += 1
        if r == word:
            print(f"Used {c} tries")

def checkinput(x):
    for i in x:
        if i not in alphabet:
            print("You have used special characters, Use alphabets only")
            return False
    return True
    

def main():
    while True:
        x = input("your word?: ")
        if checkinput(x) == True:
            character(x)
            break

if __name__ == "__main__":
    main()
    