
def get_input():
    print "Enter Number Of Columns Available in airplane:- "
    n = input()
    seat = []
    for i in range(0, n):
        print "Enter the number of rows, columns for column: " + str(i+1) + " eg.[3,2] :-"
        row_col = input()
        seat.append(row_col)
    print "Enter Number Of Passengers:-"
    passenger = input()
    return seat, passenger

def seat_structure(seat):
    string = ""
    print "\n----------  Seats In Plane Will Look Like  ----------\n"
    print "W = Window\nM = Middle\nA = Aisle\n\n********** Front **********\n"
    for i in range(0, len(seat)):
        for j in range(0, seat[i][1]):
            if(i==0 and j==0 or i==(len(seat)-1) and j == (seat[i][1])-1):
                pos = "W  "
                string = string + pos
            elif(j==0 or j==(seat[i][1]-1)):
                pos = "A  "
                string = string + pos
            else:
                pos = "M  "
                string = string + pos
        string = string + "    "
    print string            

def seat_count(seat):
    aisle = 0
    window = 0
    middle = 0
    for i in range(0, len(seat)):
        for k in range(0, seat[i][0]):
            for j in range(0, seat[i][1]):
                if(i==0 and j==0 or i==(len(seat)-1) and j == (seat[i][1])-1):
                    window += 1
                elif(j==0 or j==(seat[i][1]-1)):
                    aisle += 1
                else:
                    middle += 1
    return middle, window, aisle

def assign_seat(seat, passenger, middle, window, aisle):
    string = ""
    man = 1
    m = 0
    w = 0
    a = 0
    as_arr = []
    ws_arr = []
    ms_arr = []
    rowCount = 0
    man2 = passenger
    for i in range(1, (passenger+1)):
        if(i <= aisle):
            as_arr.append(i)
        elif(i <= (window + aisle)):
            ws_arr.append(i)
        else:
            ms_arr.append(i)
    while(passenger > 0):
        string = ""
        if(man <= man2):
            for i in range(0, len(seat)):
                for j in range(0, seat[i][1]):
                    if((i==0 and j==0 or i==(len(seat)-1) and j == (seat[i][1])-1)):
                        if(rowCount < seat[i][0] and (w < len(ws_arr))):
                            man = man + 1
                            string = string + str(ws_arr[w]) + " "
                            w += 1
                            passenger = passenger - 1
                        else:
                            string = string + "X " 
                    elif((j==0 or j==(seat[i][1]-1)) and (a < len(as_arr))):
                        if(rowCount < seat[i][0]):
                            man = man + 1
                            string = string + str(as_arr[a]) + " "
                            a += 1
                            passenger = passenger - 1
                        else:
                            string = string + "X "   
                    else:
                        if(rowCount < seat[i][0] and (m < len(ms_arr))):
                            man = man + 1
                            string = string + str(ms_arr[m]) + " "
                            m += 1
                            passenger = passenger - 1
                        else:
                            string = string + "X "   
                string = string + "    "
            print string
            rowCount = rowCount + 1
                     

if __name__ == "__main__":
    print "\n\n####### Welcome To AirPlane Seating Application #######"
    seat, passenger = get_input()
    available = 0
    for i in range(0, len(seat)):
        available += seat[i][0] * seat[i][1]

    print "Total number of seats: " + str(available) + " ;Total number of passenger: " + str(passenger)
    if(available >= passenger):
        seat_structure(seat)
        middle, window, aisle = seat_count(seat)
        assign_seat(seat, passenger, middle, window, aisle)
    else:
        print "Number of passengers are greater then number of available seats, aborting the process"
    
    

    