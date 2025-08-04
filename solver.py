import fruit_box_bot

grid = [
    [6, 2, 3, 4, 6, 4, 3, 9, 2, 9, 1, 6, 3, 1, 2, 8, 1],
    [5, 1, 5, 4, 8, 5, 2, 1, 1, 1, 1, 6, 2, 4, 2, 8, 9],
    [7, 9, 3, 2, 2, 6, 2, 2, 2, 2, 8, 4, 8, 7, 7, 9, 3],
    [7, 4, 3, 1, 8, 2, 4, 7, 6, 4, 9, 7, 1, 1, 9, 2, 8],
    [5, 1, 6, 5, 5, 5, 6, 1, 7, 6, 7, 5, 3, 1, 2, 3, 8],
    [1, 9, 8, 1, 5, 6, 9, 5, 3, 6, 5, 7, 2, 1, 7, 3, 5],
    [5, 8, 9, 5, 5, 8, 2, 4, 7, 2, 5, 2, 4, 7, 3, 9, 3],
    [2, 9, 2, 6, 4, 4, 3, 7, 2, 3, 9, 1, 3, 2, 4, 2, 2],
    [5, 4, 8, 5, 6, 8, 9, 2, 6, 2, 1, 8, 7, 3, 1, 1, 9],
    [1, 2, 4, 6, 7, 8, 2, 6, 7, 8, 5, 5, 1, 3, 1, 4, 1]
]

strategy = fruit_box_bot.find_strategy(grid)
print(f'Initial grid:')
for row in grid:
    print(row)

for step, box in enumerate(strategy.boxes, start=1):
    print(f'Step {step}: Remove box at (x={box.x}, y={box.y}) with width={box.width}, height={box.height}')
    
    for r in range(box.y, box.y + box.height):
        for c in range(box.x, box.x + box.width):
            grid[r][c] = 0
    
    print(f'Step {step}:')
    for row in grid:
        print(row)
    print()