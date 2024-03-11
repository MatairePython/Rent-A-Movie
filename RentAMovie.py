more = True
while more:
    def getdetails():
        global title, cl, genre, days
        title = input("Enter Title ")
        cl = input("Enter Classification ").lower()
        while cl != "pg" and cl != "u" and cl != "18" and cl != "12" and cl != "12a" and cl != "15":
            print("Incorrect Class ")
            cl = input("Enter Classification ")
        genre = input("Enter Genre ").lower()
        while genre != "comedy" and genre != "drama" and genre != "horror" and genre != "war" and genre != "kids":
            print("Incorrect Genre ")
            genre = input("Enter Genre ")
        days = int(input("Enter Number Of Days "))
        while days not in range(1, 11):
            print("Days must be from 1-10")
            days = int(input("Enter Number Of Days "))
            
    def calculations():
        global cost
        if genre == "kids":
            cost = 6 * days
        if genre == "drama" or "horror":
            cost = 8 * days
        if genre == "comedy" or "war":
            cost = 10 * days
            
        if days > 5:
            minus = 10 - days
            dis = minus * 0.5
            cost = cost - dis
            
    def printing():
        print("Title", title)
        print("Genre: ", genre)
        print("Rental Cost: ", cost)
        print("Period", days)
        more = input("More? y/n ")
        if more == "y":
            more = False
    
    getdetails()
    calculations()
    printing()
            

        
