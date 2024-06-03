from itertools import combinations
from sys import getsizeof


def read_file(f):
    points = []
    with open(f, "r") as points_file:
        points_list = points_file.readlines(1024)
        while points_list:
            for index in range(len(points_list)):
                data = points_list[index].replace("(", "").replace(")", "").strip().split(",")
                x = float(data[0])
                y = float(data[1])
                z = float(data[2])
                n = int(data[3])
                points.append((x, y, z, n))
            points_list = points_file.readlines(1024)
    return points

def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data    
    
def find_combinations_with_sum(points):
    valid_combinations = []
    chunk = 30
    start = 0
    end = 30
    next_chunk_start = end + 1
    next_chunk_end = next_chunk_start+chunk
    points_size = len(points) 
    while start < points_size:
        for i in range(round(points_size/chunk)):
            combos = points[start:end] # 0 - 30
            next_chunk_combos = points[next_chunk_start:next_chunk_end] # 31 - 61
            for combo in combinations(combos+next_chunk_combos, 4):
                if sum(point[-1] for point in combo) == 100:
                    volume = volume_of_tetrahedron(combo[0], combo[1], combo[2], combo[3])
                    indices = [points.index(combo[0]), points.index(combo[1]), points.index(combo[2]), points.index(combo[3]), volume]
                    if indices not in valid_combinations:
                        valid_combinations.append(indices)
            next_chunk_start = next_chunk_end + 1
            next_chunk_end += chunk if chunk < len(points[end:points_size]) else len(points[end:points_size])
        start += chunk
        end += chunk if chunk < len(points[end:points_size]) else len(points[end:points_size])   
    valid_combinations.sort(key=lambda x: x[-1])
    print(valid_combinations[0])
    print(valid_combinations[-1])
    return valid_combinations[0]

def volume_of_tetrahedron(p1, p2, p3, p4):
    # Vectors from p1 to p2, p3, and p4
    AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
    AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

    # Direct calculation of the cross product components
    cross_product_x = AB[1] * AC[2] - AB[2] * AC[1]
    cross_product_y = AB[2] * AC[0] - AB[0] * AC[2]
    cross_product_z = AB[0] * AC[1] - AB[1] * AC[0]

    # Dot product of AD with the cross product of AB and AC
    scalar_triple_product = (
        AD[0] * cross_product_x +
        AD[1] * cross_product_y +
        AD[2] * cross_product_z
    )

    # The volume of the tetrahedron
    volume = abs(scalar_triple_product) / 6.0
    return volume

def main():
    points = read_file("points_small.txt")
    find_combinations_with_sum(points)

if __name__ == "__main__":
    main()