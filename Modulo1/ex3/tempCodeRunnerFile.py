
def frequency_of_pair(file_name, relative_path):
    path = os.path.join(relative_path, file_name)
    with open(path, 'rb') as file:
        all_pairs = {}
        for line in file:
            for i in range(len(line)-1):
                pair = Pair(line[i], line[i+1])
                if (pair not in all_pairs):
                    all_pairs[pair] = 1
                else:
                    all_pairs[pair] += 1
        return all_pairs