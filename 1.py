def minion_game(string):
    stuart = 0
    kevin = 0
    for i in range(0,len(string)):
        if string[i] in 'AEIOU':
            
            kevin += len(string) - i
            print(f"kevin {kevin}")
            print(string[i:len(string)])
        else:
            
            stuart += len(string) - i
            print(f"stuart {stuart}")
            print(string[i:len(string)])
    
    if stuart == kevin:
        print("Draw")
    elif stuart>kevin:
        print("Stuart " + str(stuart))
    else:
        print("Kevin " + str(kevin))
    
if __name__ == '__main__':
    s = "ABCDCDC"
    minion_game(s)