# fruitbox-fsg
## Rules:
1. the sum has to == 0 % 10
2. the number of 9s, 8s, 7s, 6s, and half of 5s has to be at most 85 (if there is an odd number of 5s, round up)
3. there needs to be more 1s than 9s
4. the sum <= 850
all the 1s and 2s added up has to be greater than (1)number of 9s+(2)number of 8s and then so on for 7s and 6s

## Generation
**Valid Sets of Numbers:** First, we will generate all the sets of numbers that follow the stated rules. However not all of the boards created from these sets of numbers are solvable boards. Based of this set of numbers, at runtime we will randomly select one of these sets.
With this randomly selected set, we will randomize it until a solvable board is created  
**Checking the Boards:** Checking whether a board is solvable or not will be done using an algorithm created by @kevinychen

## Stack
**Backend:** The backend will be done in python and rust  
**Frontend:** I don't know probably react? or plain html/css but then it will be static which poses an issue for ranked fruitbox. C++ or Rust compiled to web assembly is also an option.

## Deploying 
I also don't know. I have seen the following things used before but we can look into more options. Also considering scalability if we make ranked.
1. Netlify: Serverless functions? I know this supports react, and it has a pretty good free tier
2. VM: AWS or Azure, both of them have the ability to create a static webpage for free, but the problem is its static. I've another VM for class that we built a vite project on but it was actually hell.
3. onrender: the thing the other fruitbox guy used? since the person also used it, it can work with vite and will work for multiplayer too.
>>>>>>> 1547c2d (pushing)
