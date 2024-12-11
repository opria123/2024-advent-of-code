from collections import defaultdict
import heapq

f = open("2024/day_09/input.txt", "r")
data = f.read()

lengths = [int(num) for num in data]

filled_grid = {} 
gaps = defaultdict(lambda: [])

cur_pos = 0
for i,num in enumerate(lengths):
    if i%2 == 0:
        filled_grid[i//2] = [cur_pos,num]
    else:
        if num > 0:
            heapq.heappush(gaps[num],cur_pos)
    cur_pos += num

for i in sorted(filled_grid.keys(),reverse=True):
    file_start_pos,file_len = filled_grid[i]
    possible_gaps = sorted([[gaps[gap_len][0],gap_len] for gap_len in gaps if gap_len>=file_len])
    if possible_gaps:
        gap_start_pos,gap_len = possible_gaps[0]
        if file_start_pos > gap_start_pos:
            filled_grid[i] = [gap_start_pos,file_len]
            remaining_gap_len = gap_len-file_len
            heapq.heappop(gaps[gap_len])
            if not gaps[gap_len]:
                del gaps[gap_len]
            if remaining_gap_len:
                heapq.heappush(gaps[remaining_gap_len],gap_start_pos+file_len)
                
answer = sum(num*(start*length+(length*(length-1))//2) for num,(start,length) in filled_grid.items()) 
print(answer)