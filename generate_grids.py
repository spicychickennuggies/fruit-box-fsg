import json
import fruit_box_bot
import random
import numpy as np

def main():
    score = 0
    
    print("begin loading")
    load = np.load("combination6.npz")
    combo_values = load['data']
    
    
    print("finished loading")
    
    
    
    for i in range(5):
        grid = []
        while score < 170:
            counts = combo_values[random.randint(0, len(combo_values))]
            
            print(counts)
            
            np_grid = np.zeros(170, dtype=np.int64)
            start = 0
            for i in range(0, 8):
                np_grid[start:start+counts[i]] = i+1
                start += counts[i]
            np_grid[start:170] = 9
            
            np.random.shuffle(np_grid)
            grid = np.reshape(np_grid, (10, 17)).tolist()
                    
            strategy = fruit_box_bot.find_strategy(grid)
            score = strategy.score
                    
        print(grid)
        
if __name__ == '__main__':
    main()