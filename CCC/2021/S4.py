#Daily Commute, works for the first sample case
walkways = []
route = None
changes = []
day = 0
minutes = 0



#input
number_stations, number_walkways, days = map(int, input().split(" "))

for i in range(number_walkways):
    walkways.append(list(map(int, input().split(" "))))

route = list(map(int, input().split(" ")))

for i in range(days):
    changes.append(list(map(int, input().split(" "))))
    
def change_stations(day):
    global route, changes
    
    one, two = changes[day]
    
    temp = route[one-1]
    route[one-1] = route[two-1]
    route[two-1] = temp
    
def find_route(station, time):
    global number_stations, visited
    time += 1
    if visited[station]:
        return None
    else:
        visited[station] = True
        for i in range(number_stations-1):
            
            if walkways[i][0] == station:
                #print("SAME STATION")
                #print(walkways[i][0])
                #print(walkways[i][1])
                if walkways[i][1] == number_stations:
                    #print("HEHEhE " + str(time))
                    return time
                else:
                    result = find_route(walkways[i][1], time)
                    
                    if result is not None:
                        return result
            
        
for i in range(days):
    change_stations(i)
    minutes = route.index(number_stations)
    #print("CURRENT TIME" + str(minutes))
    #print(route)
    for i in range(minutes):
        visited = [False] * number_stations
        potential_route = find_route(route[i], i)
        #print(potential_route)
        if potential_route == None:
            potential_route = 10000000000
        minutes = min(potential_route, minutes)
    
    print(minutes)
    

    
    
    
    
    
    