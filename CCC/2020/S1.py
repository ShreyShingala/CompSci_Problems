# Surmising a Sprinter’s Speed

times = []
speeds = []

for i in range(int(input())):
    times.append(list(map(int, input().split(" "))))
    
    
times.sort(key=lambda x: x[0])

for i in range(len(times)-1):
    speeds.append(abs(times[i][1] - times[i+1][1]) / abs(times[i][0] - times[i+1][0]))
    
print(max(speeds))