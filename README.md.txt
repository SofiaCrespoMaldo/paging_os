Sofia I. Crespo Maldonado
Assignment 3: Memory Management
CCOM4017: Operating Systems
Prof. Jose R. Ortiz-Ubarri

CONTENTS
--------

- Introduction
- Prerequisites
- FIFO Algorithm
- Optimal Replacement Algorithm
- Working Set Clock Replacement Algorithm
- Resources


INTRODUCTION
------------

This project is a simulation of 3 page replacement algorithms in order to get 
familiarized with Memory Management in Operating Systems. The systems will read
a file with a sequence of virtual page access requests, placing each requested
page on Physical memory and replacing pages whenever memory is full. They must
keep track of page faults whenever a page is brought into memory.


PREREQUISITES
-------------

- Python: www.python.org


FIFO ALGORITHM
--------------

The FIFO algorithm replaces the first page inserted in Physical Memory whenever
the memory is full and the requested page is not in memory. It's implementation
is on fifo.py.

The simulations must be ran as follows:
	python fifo.py <Number of physical memory pages> <Access sequence file>

Example:
	python fifo.py 10 requests.txt

Variables:
- N: number of Physical Memory pages
- p_memory: list of size N to store the requested pages
- file: string to store access sequene file name
- f: text stream to read file from
- p_faults: counter for number of page faults
- empty: number of empty pages left in Physical Memory
- found: marks if a page is in memory

main():
- Reads input from terminal
- Opens and reads file
- Checks if page request is in memory
- Inserts in Physical Memory if there's space
- Calls fifo(req, p_memory, N) if Physical Memory is full

fifo(req, p_memory, N):
- Shifts the pages in memory one space down, thus removing first page inserted
- Enters requested page on the last space of Physical Memory


OPTIMAL REPLACEMENT ALGORITHM
-----------------------------

The Optimal Replacement algorithm replaces the page that will be accessed the
furthest in the further in the list of memory accesses, or not accessed at all.
It's implementation is on optimal.py.


The simulations must be ran as follows:
	python optimal.py <Number of physical memory pages> <Access sequence file>

Example:
	python optimal.py 10 requests.txt

Variables:
- N: number of Physical Memory pages
- p_memory: list of size N to store the requested pages
- file: string to store access sequene file name
- f: text stream to read file from
- p_faults: counter for number of page faults
- empty: number of empty pages left in Physical Memory
- found: marks if a page is in memory
- index: position of page request
- reused: marks if a page is reused further in memory access list
- furthest: page that is accessed furthest in memory access list

main():
- Reads input from terminal
- Opens and reads file
- Checks if page request is in memory
- Inserts in Physical Memory if there's space
- Calls optimal(reqs, index, p_memory, N) if Physical Memory is full

optimal(reqs, index, p_memory, N):
- Traverses Physical memory and compares with memory access list from current
request onward, remembering the page with furthest access
- If it finds a page that does not get accessed, it chooses to replace that one


WORKING SET CLOCK REPLACEMENT ALGORITHM
---------------------------------------

The WSClock algorithm uses a system clock and a parameter tau. The working set
uses an interval of time (tau) that is used to make decisions regarding the page
replacement (to check whether the page is in the working set). A clock is kept 
(same size as Physical Memory) to record the time at which a page in memory was
last accessed and a reference bit to check whether it was referenced (1 or 0). 
Each page request equals a tick of the clock. It's implementation is on 
wsclock.py.


The simulations must be ran as follows:
	python wsclock.py <Number of physical memory pages> <tau> <Access sequence file>

Example:
	python wsclock.py 10 3 requests.txt

Variables:
- N: number of Physical Memory pages
- tau: interval of time parameter
- p_memory: list of size N to store the requested pages
- clock: 2d list of size N to store time of last access and reference bit
- file: string to store access sequene file name
- f: text stream to read file from
- p_faults: counter for number of page faults
- empty: number of empty pages left in Physical Memory
- curr_time: system clock
- pointer: clock hand, moves when there's a page fault
- found: marks if a page is in memory
- oldest: smallest time in clock
- old_ind: index of oldest
- age: time since last access

main():
- Reads input from terminal
- Opens and reads file
- Checks if page request is in memory
- Inserts in Physical Memory if there's space and updates clock
- Calls wsclock(req, curr_time, pointer, clock, p_memory, tau, N) if Physical
Memory is full

wsclock(req, curr_time, pointer, clock, p_memory, tau, N):
- Checks if page was not referenced and not on working set, it replaces it
- If all the pages have been referenced, it traverses the clock remembering the
oldest page access time and changes the reference bit of each page to 0
- Replaces oldest accessed page in Physical Memory and updates clock time with
the current time and sets reference bit to 1


RESOURCES
---------
- https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
- https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
- https://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
- https://discuss.python.org/t/change-a-argument-value-of-a-function-without-returning/14715/2