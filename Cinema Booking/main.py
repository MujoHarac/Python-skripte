import math, random, time, os, sys


cinema_seats = []

ROW_CINEMA = 15
COL_CINEMA = 8


class Cinema:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col

class Style:
    END_COLOR = '\x1b[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def create_cinema_nestedList(row_cinema, col_cinema):
    _copy_of_row_cinema = row_cinema
    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    occupied = Style.RED + "1" + Style.END_COLOR

    
    for i in range(row_cinema):
        _cinemaRow = []
        for j in range(col_cinema):
            _cinemaRow.append(0)
        cinema_seats.append(_cinemaRow)

    number_rows_first_zone = math.floor(_copy_of_row_cinema / 3)
    
    _copy_of_row_cinema -= number_rows_first_zone
    
    number_rows_lover_zone = math.floor(_copy_of_row_cinema / 3)

    _copy_of_row_cinema -= number_rows_lover_zone

    number_rows_second_zone = _copy_of_row_cinema

    first_zone = cinema_seats[ : number_rows_first_zone]
    second_zone = cinema_seats[number_rows_first_zone : number_rows_second_zone+number_rows_first_zone]
    lover_zone = cinema_seats[number_rows_second_zone+number_rows_first_zone : ]

    #print('first',first_zone)
    #print('second',second_zone)
    #print('third',lover_zone)

    seats = [not_occupied,occupied]
    #random occupied seats in first zone
    for i,j in enumerate(first_zone):
        for k,l in enumerate(j):
            num_random = random.choice(seats)
            first_zone[i][k] = num_random

    #random occupied seats in second zone
    for i,j in enumerate(second_zone):
        for k,l in enumerate(j):
            num_random = random.choice(seats)
            second_zone[i][k] = num_random

    #random occupied seats in lovers zone
    for i,j in enumerate(lover_zone):
        for k,l in enumerate(j):
            num_random = random.choice(seats)
            lover_zone[i][k] = num_random

    


    return number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone
   

def main_menu(name):
    while True:
        os.system("cls")
        stringer_noAdmin = f"""{Style.END_COLOR}
            -_-_-_-_-_-   {Style.MAGENTA}WELCOME TO {name} CINEMA{Style.END_COLOR}   -_-_-_-_-_-
        Current account: {Style.RED}none{Style.END_COLOR}   -type: Admin login--
                        
                        Cinema Hall is divided in to 3 zones, first two are regular ones and the third one is lover zone, it's for couples,
                        lovers and anyone who wants to be alone
                        {Style.RED}if you want to end the booking session type: end{Style.END_COLOR}

                                1. Show current hall
                                2. Book a seat
                                3. Book from the front(first available seat in first two zones)
                                4. Book from the back(first available seat in first two zones)

        
        
                        """
        print(stringer_noAdmin)
        num = input( Style.BLUE + "Type the number what you want to do: "+Style.END_COLOR)
        if num == "end":
            return "end"
        elif num.isnumeric() and int(num) in range(1,4+1):
            return int(num)
        elif num.lower() == "admin login":
            return 0
        else: continue
    
        

def draw_cinema(number_rows_first_zone, number_rows_second_zone,col_cinema):
    os.system("cls")
    print("    ", end="")#space before col numbers
    
    #Numbers representing col number 
    print(" ", end= "")
    for i in range(1,col_cinema+1):
        if i < 10:
            print(f" {i}", end=" ")
            bina_decorator = col_cinema + 4
        elif i >= 10:
            print(f"{i}", end=" ")
            bina_decorator = col_cinema + 6
    print("")
    print("    " +"<>"*bina_decorator)
    
    #main loop over cinema_seats 
    for i,j in enumerate(cinema_seats, start=1):
        if i == number_rows_first_zone+1:
            #passage between 2 zones for pedestrians
            print("   "+"--"*(bina_decorator+1))
            print(" "*len(j))
            print("   "+"--"*(bina_decorator+1))
        elif i == number_rows_first_zone + number_rows_second_zone+1:
            #passage between 2 zones for pedestrians
            print("   "+"--"*(bina_decorator+1))
            print(" "*len(j))
            print("   "+"--"*(bina_decorator+1))
        #Side row numbers and left wall |
        print(f"{i:>2} ", end="")
        print("|", end="")
        for k,l in enumerate(j):
            print(f"  {l}", end="")
            if k == len(j)-1:
                #right wall
                print("|", end="")
        print("")

def booking(row_cinema, col_cinema):
    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    occupied = Style.RED + "1" + Style.END_COLOR
    current_session_occupied = Style.YELLOW + "1" + Style.END_COLOR
    while True:
        check = input(f"{Style.BLUE}Type your what seat you wish to take(first: row col): {Style.END_COLOR}")
        check = check.split(" ")
        if not len(check) == 2:
            continue
        if not check[0].isnumeric() or not check[1].isnumeric:
            continue
        elif int(check[0]) > row_cinema or int(check[1]) > col_cinema:
            continue
        input_row = int(check[0])
        input_col = int(check[1])
        if cinema_seats[input_row-1][input_col-1] == occupied:
            print("That seat is occupied, pick another")
        elif cinema_seats[input_row-1][input_col-1] == current_session_occupied:
            cinema_seats[input_row-1][input_col-1] = not_occupied
            break
        else: 
            cinema_seats[input_row-1][input_col-1] = current_session_occupied
            break
    return input_row, input_col

def book_from_front(number_rows_first_zone, number_rows_second_zone):
    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    occupied = Style.RED + "1" + Style.END_COLOR
    current_session_occupied = Style.YELLOW + "1" + Style.END_COLOR

    for i,j in enumerate(cinema_seats[ : number_rows_first_zone + number_rows_second_zone]):
        for k,l in enumerate(j):
            if cinema_seats[i][k] == not_occupied:
                cinema_seats[i][k] = current_session_occupied
                return i, k
            elif i == number_rows_first_zone + number_rows_second_zone:
                print("First two zones are out of capacity")
                time.sleep(2)
                
def booking_from_the_back(number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone):
    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    occupied = Style.RED + "1" + Style.END_COLOR
    current_session_occupied = Style.YELLOW + "1" + Style.END_COLOR
    
    row_index = len(cinema_seats)-number_rows_lover_zone
    col_index = len(cinema_seats[0])-1
    while True:
        for i in range(number_rows_first_zone + number_rows_second_zone):
            for k in range(len(cinema_seats[0])):
                if cinema_seats[row_index-1][col_index] == not_occupied:
                    cinema_seats[row_index-1][col_index] = current_session_occupied
                    return row_index, col_index
                elif col_index == 0:
                    row_index -= 1
                    col_index = len(cinema_seats[0])-1
                else:
                    col_index -= 1
                if row_index < 1:
                    print("First two zones are out of capacity")
                    time.sleep(2)
                    return 

def admin_log_in():
    user = ''
    password = ''
    with open("admins_for_cinema.csv", "r") as f:
        for line in f:
            user,password = line.split(",")
    print(user, password)
    admin_username = input("Enter user name: ")
    if admin_username != user:
        print("Wrong user name!")
        time.sleep(1)
        return False
    admin_password = input("Enter password: ")
    if admin_password != password.strip():
        print("Wrong password!")
        time.sleep(1)
        return False
    
    return user, password

def admin_main_menu(cinema, user):
    admin_name = user[0]
    os.system("cls")
    stringer_Admin = f"""{Style.END_COLOR}
            -_-_-_-_-_-   {Style.BLACK}WELCOME TO {cinema} CINEMA{Style.END_COLOR}   -_-_-_-_-_-
        Current account: {Style.RED}{admin_name}{Style.END_COLOR} 
                        
                        With great power comes great responsibility
                        {Style.RED}if you want to end the admin session type: end{Style.END_COLOR}

                                1. Reset cinema hall
                                2. Percentage of bought tickets
                                3. Change row and col of cinema hall
                                4. Add another Admin account
                        """
    print(stringer_Admin)
    while True:
            num = input( Style.BLUE + "Type the number what you want to do: "+ Style.END_COLOR)
            if num.isnumeric() and int(num) in range(1,4+1):
                return int(num)
            elif num == "end":
                return "end"
            else: continue

def reset_hall():
    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    for i,j in enumerate(cinema_seats):
        for k,l in enumerate(j):
            cinema_seats[i][k] = not_occupied

def percentage_bought_tickets():
    not_occupied = Style.GREEN + '0' + Style.END_COLOR
    bought = 0
    empty = 0
    all_seats = 0
    for i,j in enumerate(cinema_seats):
        for k,l in enumerate(j):
            all_seats += 1
            if cinema_seats[i][k] == not_occupied:
                empty += 1
            else: 
                bought += 1
    perc = (bought/all_seats)*100
    print(f"Percentage of bought tickes is {perc}%")
    time.sleep(2)

def change_size_of_cinema():
    print(f"{Style.RED}This could take a while, maybe days or even years. Just imagen trying to remodel 10x10 cinema in to 50x50, jeeeeez...don't go to crazy{Style.END_COLOR}")
    input(f"{Style.BLUE}Press Enter{Style.END_COLOR}")
    while True:
        num_row = input("{Style.BLUE}How many rows do you want new cinema to have{Style.END_COLOR}")
        if num_row.isnumeric():
            break
    while True:
        num_col = input("{Style.BLUE}How many cols do you want new cinema to have{Style.END_COLOR}")
        if num_col.isnumeric():
            break
    while True:
        new_name = input("{Style.BLUE}What is the name of our new cinema: {Style.END_COLOR}")
        if not new_name.isnumeric():
            break
    print(f"{Style.BLUE}Your new cinema is called{Style.END_COLOR} {Style.RED}{new_name}{Style.END_COLOR} {Style.BLUE}and it's {Style.BLUE}{num_row}x{num_col}{Style.END_COLOR}")
    yes_no = input("{Style.BLUE}Are you satisfied?(yes or no)")
    while True:
        if yes_no.lower() == "yes":
            return new_name, num_row, num_col
        elif yes_no.lower() == "no":
            change_size_of_cinema()




def main(row_cinema=8, col_cinema=6):
    global cinema_seats
    cinema_name = "Star"
    cinema = Cinema(cinema_name, row_cinema, col_cinema)
    current_session_tickets = []
    number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone = create_cinema_nestedList(row_cinema, col_cinema)
    while True:    
        choice = main_menu(cinema_name)
        if choice == 1: #Show current hall
            draw_cinema(number_rows_first_zone, number_rows_second_zone, col_cinema)
            input(f"{Style.BLUE}Press Enter{Style.END_COLOR}")
            continue

        elif choice == 2:                                                                   #Book a seat
            draw_cinema(number_rows_first_zone, number_rows_second_zone, col_cinema)
            picked_row, picked_col = booking(row_cinema, col_cinema)
            current_session_tickets.append((picked_row, picked_col))

        elif choice == 3:                                                                   #Book from the front(first available seat in first two zones)
            picked_row_col = book_from_front(number_rows_first_zone, number_rows_second_zone)
            current_session_tickets.append(picked_row_col)

        elif choice == 4:                                                                   #Book from the back(first available seat in first two zones)
            picked_row_col = booking_from_the_back(number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone)
            current_session_tickets.append(picked_row_col)

        elif choice == 0:
                                                                               #you've typed in `admin login`
            user = admin_log_in()
            if user == False:
                continue
            while True:
                admin_choice = admin_main_menu(cinema_name, user)
                if admin_choice == "end":
                    break
                elif admin_choice == 1:                               #Reset cinema hall
                    reset_hall()
                    draw_cinema(number_rows_first_zone, number_rows_second_zone, col_cinema)
                    input(f"{Style.BLUE}Press Enter{Style.END_COLOR}")
                elif admin_choice == 2:                             #Percentage of bought tickets
                    percentage_bought_tickets()
                elif admin_choice == 3:                             #Change row and col of cinema hall
                    new_name, num_row, num_col = change_size_of_cinema()
                    cinema_name = new_name
                    row_cinema = int(num_row)
                    col_cinema = int(num_col)
                    cinema_seats = []
                    number_rows_first_zone, number_rows_second_zone, number_rows_lover_zone = create_cinema_nestedList(row_cinema, col_cinema)
        elif choice == "end":
            draw_cinema(number_rows_first_zone, number_rows_second_zone, col_cinema)
            for i in current_session_tickets:
                if i == None:
                    continue
                print(f"{Style.MAGENTA}Tickets you've bought: {i[0]+1,i[1]+1}{Style.END_COLOR}")
            sys.exit()

if __name__ == "__main__":
    main(ROW_CINEMA, COL_CINEMA)