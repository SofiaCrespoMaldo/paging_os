# Sofia I. Crespo Maldonado
# CCOM4017: Operating Systems
# Assignment 3: Memory Management

import sys

def wsclock(req, curr_time, pointer, clock, p_memory, tau, N):
    oldest = clock[pointer][0] # smallest time in clock
    old_ind = pointer # index of smallest time

    for i in range(N+1): 
        age = curr_time - clock[pointer][0] # calculate age of the page

        if (clock[pointer][0] < oldest): # if its the oldest page, update variables
            oldest = clock[pointer][0]
            old_ind = pointer
            
        if (clock[pointer][1] == 0 and age > tau): # Not referenced and not in working set
            p_memory[pointer] = req # replace page with new request
            clock[pointer][0] = curr_time # set time of last access
            clock[pointer][1] = 1 # set reference bit to 1
            if (pointer == N-1): # next spot in the clock
                pointer = 0
            else: pointer+=1
            return pointer

        elif (clock[pointer][1] == 1): # if page was referenced
            clock[pointer][1] = 0 # change reference bit to 0
            if (pointer == N-1): # next spot in the clock
                pointer = 0
            else: pointer+=1
            continue

    # Replace oldest page and set time and reference bit
    clock[old_ind][1] = 1
    clock[old_ind][0] = curr_time
    p_memory[old_ind] = req
    return pointer
        
def main():
    N = int(sys.argv[1]) # Pages in physical memory
    tau = int(sys.argv[2]) # interval of time for working set
    p_memory = [None]*N # Physical Memory
    clock = [[None]*2 for _ in range(N)] # stores time of last access of a page and reference bit
    file = sys.argv[3] # File name

    # Opening, reading contents and closing file
    f = open(file, 'r')
    requests = [int(n.strip(' WR:')) for n in f.read().split()] # Convert memory access sequence to list of integers
    f.close()

    p_faults = 0 # Counter for requests that are not in memory
    empty = N # spots available in memory
    curr_time = 1 # initialize system clock
    pointer = 0 # represents the hand of the clock


    for j in range(len(requests)): # for each page access request
        found = 0 # indicates whether the page is in memory(1) or not(0)
        
        if (j == 0): # for the first request
            p_faults+=1 # page is not in memory, add to counter
            p_memory[0] =  requests[j] # insert page to memory
            clock[0][0] = curr_time # record time of access
            clock[0][1] = 1 # page has been referenced
            empty-=1 # substract from spaces available in memory
            curr_time+=1 # next tick of the clock
            pointer+=1 # next spot in clock
            continue # go to next request

        for i in range(N): # check if the page is in memory
            if (p_memory[i] == requests[j]): # if page is in memory, stop checking
                found = 1 # page is found in memory
                clock[i][0] = curr_time # update time of last access
                clock[i][1] = 1 # page has been referenced
                curr_time+=1 # next tick of the clock
                break

        if (found == 0 and empty > 0): # when there's still space in memory
            p_faults+=1 # page is not in memory, add to counter

            for i in range(N): # traverse memory until it finds an empty slot
                if (p_memory[i] == None): # finds empty space and places request there
                    p_memory[i] = requests[j]
                    clock[i][0] = curr_time # update time of last access
                    clock[i][1] = 1 # page has been referenced
                    empty-=1 # substract from spaces available in memory
                    curr_time+=1 # next tick of the clock
                    if (pointer == N-1): pointer = 0 # next spot in the clock
                    else: pointer+=1
                    break
            continue # go onto next request
        
        
        elif (empty == 0 and found == 0): # when page is not in memory and memory is full
            p_faults+=1 # page is not in memory, add to counter
            pointer = wsclock(requests[j], curr_time, pointer, clock, p_memory, tau, N) # call page replacement algorithm
            curr_time+=1 # next tick of the clock


    print("\nPhysical Memory Status\n", p_memory, "\n")
    print("Total of page faults: ", p_faults)

if __name__ == "__main__":
    main()