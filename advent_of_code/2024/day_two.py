def main(path):
    return get_total_safe_rows(path)
def get_total_safe_rows(path):
    total = 0
    with open(path) as f:
        row = f.readline().rstrip('\n')
        while row:
            if get_level_is_safe(row):
                total += 1
            else:
                row = remove_first_unsafe_level(row)
                if get_level_is_safe(row):
                    total += 1
            row = f.readline().rstrip('\n')
    return total

def remove_first_unsafe_level(row):
    row = row.split(" ")
    row = [int(x) for x in row]
    # check if all increasing or decreasing first
    is_increasing = row == sorted(row) 
    is_decreasing = row == sorted(row, reverse=True)
    if is_increasing:
        for i in range(len(row)-1):
            j = i + 1
            diff = abs(row[i]-row[j])
            if diff == 0 or diff > 3:
                row.pop(i)
                return row
    elif is_decreasing:
        for i in range(len(row)-1):
            j = i + 1
            diff = abs(row[i]-row[j])
            if diff == 0 or diff > 3:
                row.pop(j)
                return row
    else:
    
        if row != set(row):
            #check for duplicates
            print(f'checking row: {row} for duplicates')
            new_row = []
            set_row = set(row)
            for i, num in enumerate(row):
                if num in set_row:
                    new_row.append(num)
                    set_row.remove(num)
                else:
                    break
            new_row += row[i+1:]
            return new_row                    
        print(f'row: {row} is not increasing, decreasing, and has no duplicates but is not safe')
        #need to check for some additional possibilities here
        # remove first item that is not increasing and check for remaining set being increasing
        for i in range(len(row) -1 ):

            print('found one that should be all increasing after removing one value')
            j = i + 1
            if row[i] > row[j] and row[j:] == sorted(row[j:]):
                row.pop(i)
                return row
        # same but for decreasing
        for i in range(len(row) -1 ):
            print('found one that should be all decreasing after removing one value')
            j = i + 1
            if row[i] < row[j] and row[j:] == sorted(row[j:], reverse=True):
                row.pop(i)
                return row
    return row


def get_level_is_safe(row):
    if isinstance(row, str):
        row = row.split(" ")
        row = [int(x) for x in row]
    #check if all increasing or all decreasing
    if row == sorted(row) or row == sorted(row, reverse=True):
        for i in range(len(row)-1):
            j = i + 1
            diff = abs(row[i]-row[j])
            if diff == 0 or diff > 3:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    print(main("day_two.txt"))
