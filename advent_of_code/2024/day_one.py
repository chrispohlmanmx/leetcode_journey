def main(path):
    a, b = get_sorted_lists(path)
    print(total_differences(a,b))
    print(get_similarity_scores(a,b))


def get_sorted_lists(path):
    left_list = []
    right_list = []

    with open(path) as f:
        row = f.readline()
        while row:
            row = row.rstrip('\n')
            nums = row.split(" ")
            left_list.append(int(nums[0]))
            right_list.append(int(nums[-1]))
            row = f.readline()
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    return sorted_left, sorted_right

def total_differences(sorted_left, sorted_right):
    differences = []
    for i in range(len(sorted_left)):
        difference = abs(sorted_left[i]-sorted_right[i])
        differences.append(difference)
    total = sum(differences)

    return total

def get_similarity_scores(left, right):
    appearences = {}

    for num in left:
        for num_2 in right:
            if num == num_2:
                if num in appearences.keys():
                    appearences[num] += 1
                else:
                    appearences[num] = 1
        if num not in appearences.keys():
            appearences[num] = 0
    score = 0
    for num in left:
        to_add = num * appearences[num]
        score += to_add 
    return score

if __name__ == "__main__":
    (main('day_one.txt'))

