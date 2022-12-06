def task(line, marker_lenght):
    marker = []
    for count, char in enumerate(line):
        if count < marker_lenght:
            marker += char
        else:
            for signal in marker:
                if marker.count(signal) > 1:
                    fertig = False
                    break
                else:
                    fertig = True
            if fertig:
                print(count)
                return(count)
            else:
                marker += char
                del marker[0]
    
with open("input.txt", "r") as f:
    for line in f:
            task(line, 4)
            task(line, 14)
                