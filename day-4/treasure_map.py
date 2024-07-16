line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
valid_positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
location_index_map = {"A": 0,"B": 1,"C": 2}

print("Hiding your treasure! X marks the spot.")

position = input()

if position not in valid_positions:
  print("Invalid position. Try again.")
  print(f"Valid positions are {valid_positions}")
  exit(1)

location_in_array = location_index_map[position[0]]
line_index = int(position[1]) - 1

map[line_index][location_in_array] = "X"

print(f"{line1}\n{line2}\n{line3}")
