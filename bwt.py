import sys
# first_column_index = open('chrX_map.txt', 'r').readlines()
# first_column_file = open('chrX.fa', 'r').read().replace('\n', '')
# first_column_file_len = len(first_column_file)
# # print(last_col_file)
# print(first_column_file[first_column_file_len-1])
# rank = {'A': [],
#         'C': [],
#         'G': [],
#         'T': []}

# count = 1
# for index in first_column_index:
#     index_ = int(index.strip())+5
#     if index_ >= first_column_file_len:
#         index_ -= 1
#     character = first_column_file[index_]
#     # print(character)
#     if count % 100 == 0:
#         if character in rank:
#             rank[character].append(count)
#     count += 1

delta = 15

last_column_file = open('data/chrX_last_col.txt', 'r').read()

occurance_of_characters = {base:[False for i in range(len(last_column_file))] for base in ['A', 'T', 'C', 'G']}

length_of_last_column_file = len(last_column_file)

# occurance_A = [False for i in range(len(length_of_last_column_file))]
# occurance_C = [False for i in range(len(length_of_last_column_file))]
# occurance_G = [False for i in range(len(length_of_last_column_file))]
# occurance_T = [False for i in range(len(length_of_last_column_file))]

rank_of_characters = {base:[] for base in ['A','T','C','G']}

# rank_A = []
# rank_C = []
# rank_G = []
# rank_T = []

index = 0

count_of_characters = {base:0 for base in ['A', 'T', 'C', 'G']}

# count_A = 0
# count_C = 0
# count_G = 0
# count_T = 0

while(index < length_of_last_column_file):
    character = last_column_file[index]
    if(not character):
        break
    if(character!='$' and character!='\n'):
        occurance_of_characters[character][index] = True
        count_of_characters[character]+=1
        # if character == 'A':
        #     occurance_A[index] = True
        # elif character == 'C':
        #     occurance_C[index] = True
        # elif character == 'G':
        #     occurance_G[index] = True
        # elif character == 'T':
        #     occurance_T[index] = True

        if(index > 0 and index % delta == 0):
            for b in ['A', 'T', 'C', 'G']:
                rank_of_characters[b].append(count_of_characters[b])
            # rank_A.append(count_A)
            # rank_C.append(count_C)
            # rank_G.append(count_G)
            # rank_T.append(count_T)
    
    index += 1

def rank(char, index, delta):
    print(f'Rank of chr {char} at index {index}')
    if index % delta == 0:
        return rank_of_characters[char][int(index/delta)]
    else:
        if index % delta > delta / 2:
            lower_limit = index
            upper_limit = index + (delta - (index % delta))
            rank_index = int(upper_limit/delta)
            return rank_of_characters[char][rank_index-1] - occurance_of_characters[char][lower_limit+1:upper_limit+1].count(True)
        else:
            lower_limit = index - (index % delta)
            upper_limit = index
            rank_index = int(lower_limit/delta)
            if rank_index == 0:
                return occurance_of_characters[char][lower_limit:upper_limit+1].count(True)
            else:    
                return rank_of_characters[char][rank_index-1] + occurance_of_characters[char][lower_limit:upper_limit+1].count(True)

print(rank('C', 500, delta))
print(rank('C', 700, delta))
print(rank('C', 900, delta))
print(rank('C', 1600, delta))
print(rank('C', 5000, delta))
print(rank('C', 7000, delta))
print(rank('C', 9000, delta))
print(rank('C', 16000, delta))

# print(sys.getsizeof(occurance_of_characters['A']) +
#         sys.getsizeof(occurance_of_characters['C'])+
#         sys.getsizeof(occurance_of_characters['G'])+
#         sys.getsizeof(occurance_of_characters['T']))

# print(sys.getsizeof(rank_of_characters['A']) + 
# sys.getsizeof(rank_of_characters['C']) +
# sys.getsizeof(rank_of_characters['G']) +
# sys.getsizeof(rank_of_characters['T']))