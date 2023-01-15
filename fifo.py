# Sofia I. Crespo Maldonado
# CCOM4017: Operating Systems
# Assignment 3: Memory Management

import sys

def fifo(req, p_memory, N):
    for i in range(N-1): # traverse memory
        p_memory[i] = p_memory[i+1] # shift each value to the left
    
    p_memory[N-1] = req # place new page on last spot

def main():
    N = int(sys.argv[1]) # Pages in physical memory
    p_memory = [None]*N # Physical Memory
    file = sys.argv[2] # File name

    # Opening, reading contents and closing file
    f = open(file, 'r')
    requests = [int(n.strip(' WR:')) for n in f.read().split()] # Convert memory access sequence to list of integers
    f.close()

    p_faults = 0 # Counter for requests that are not in memory
    empty = N # spots available in memory

    for j in range(len(requests)): # for each page access request

        found = 0 # indicates whether the page is in memory(1) or not(0)
        
        if (j == 0): # for the first request
            p_faults+=1 # page is not in memory, add to counter
            p_memory[0] =  requests[j] # insert page to memory
            empty-=1 # substract from spaces available in memory
            continue # go to next request

        for i in range(N): # check if the page is in memory
            if (p_memory[i] == requests[j]): # if page is in memory, stop checking
                found = 1 # page is found in memory
                break

        if (found == 0 and empty > 0): # when there's still space in memory
            p_faults+=1  # page is not in memory, add to counter

            for i in range(N): # traverse memory until it finds an empty slot
                if (p_memory[i] == None): # finds empty space and places request there
                    p_memory[i] = requests[j]
                    empty-=1 # substract from spaces available in memory
                    break # stop traversing once page has been inserted
            continue # go onto next request
        
        
        elif (empty == 0 and found == 0): # when page is not in memory and memory is full
            p_faults+=1  # page is not in memory, add to counter

            fifo(requests[j], p_memory, N) # call page replacement algorithm

    print("\nPhysical Memory Status\n", p_memory, "\n")
    print("Total of page faults: ", p_faults)



if __name__ == "__main__":
    main()