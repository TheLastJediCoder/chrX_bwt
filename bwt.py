# bit_array = {'A': [], 'C': [], 'G': [], 'T': []}
bit_array = []
rank = {'A': [0], 'C': [0], 'G': [0], 'T': [0]}
total = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
delta = [15]

last_col_file = open('data/chrX_last_col.txt', 'r')

i = 0
while(True):
    char = last_col_file.read(1)
    if char == '\n':
        char = last_col_file.read(1)
    if i == delta[0]:
        rank['A'].append(total['A'])
        rank['C'].append(total['C'])
        rank['G'].append(total['G'])
        rank['T'].append(total['T'])
        i = 0
    
    if char in total:
        total[char] += 1

    bit_array.append(char)
    # bit_array['A'].append(True if char == 'A' else False)
    # bit_array['C'].append(True if char == 'C' else False)
    # bit_array['G'].append(True if char == 'G' else False)
    # bit_array['T'].append(True if char == 'T' else False)

    if not char:
        break
    i += 1

def rank_last_col(char, index):
    # if index > len(bit_array['A']) or index < 0:
    if index > len(bit_array) or index < 0:
        print('Index out of bound')
        return -1
    delta_index = int(index / delta[0])
    delta_index_mult = int(delta_index * delta[0])
    res = 0
    res = rank[char][delta_index]
    for j in range(delta_index_mult, index):
        # if bit_array[char][j]:
        #     res += 1
        if bit_array[j] == char:
            res += 1
    return res

band = {}
band['A'] = 0
band['C'] = total['A']
band['G'] = total['A'] + total['C']
band['T'] = total['A'] + total['C'] + total['G']

def select_first_col(i, char):
    return band[char] + i - 1

def map_read(reads):
    char = reads[-1]
    band_start = select_first_col(1, char)

    count = total[char]   
    band_end = select_first_col(count, char)

    for i in range(len(reads)-2, -1, -1):
        # print(band_start, band_end)
        top = rank_last_col(reads[i], band_start)
        bottom = rank_last_col(reads[i], band_end)
        # print(top, bottom, reads[i])
        bottom_inclusive = bottom
        # if (bit_array['A'][band_end] and reads[i] == 'A') or (bit_array['C'][band_end] and reads[i] == 'C') or (bit_array['G'][band_end] and reads[i] == 'G') or (bit_array['T'][band_end] and reads[i] == 'T'):
        #     bottom_inclusive += 1
        if (bit_array[band_end] == 'A' and reads[i] == 'A') or (bit_array[band_end] == 'C' and reads[i] == 'C') or (bit_array[band_end] == 'G' and reads[i] == 'G') or (bit_array[band_end] == 'T' and reads[i] == 'T'):
            bottom_inclusive += 1
        if bottom_inclusive == top:
            return -1, -1
        band_start = select_first_col(top+1, reads[i])
        band_end = select_first_col(bottom_inclusive, reads[i])
    
    return band_start, band_end

read = 'TGGCCAAATCTTAGCTATTTGAGGAATGTAGGGAGAAAAGCCACCTTCTCTCTCTATGTCTGAAGGTTCCCATGGCTGTCTCTTTGCCCAAGGGGCAAACT'
positions = map_read(read)

get_index_to_reference_sequence = open('data/chrX_map.txt', 'r').readlines()
reference_file = open('data/chrX.fa', 'r').read().replace('\n', '')
index_to_reference_sequence = int(get_index_to_reference_sequence[positions[0]].strip())
reference_read = reference_file[index_to_reference_sequence:index_to_reference_sequence+len(read)]

print(f'Positions      : {positions}')
print(f'Index in rfile : {index_to_reference_sequence}')
print(f'Actual Read    : {read}')
print(f'Reference Read : {reference_read}')
print(f'Match?         : {read == reference_read}')