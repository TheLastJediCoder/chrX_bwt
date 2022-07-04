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

last_col_file = open('chrX_last_col.txt', 'r')
last_col_arr = {base:[] for base in ['A', 'T', 'C', 'G']}
rank_arr = {base:[] for base in ['A','T','C','G']}
delta = 5

local_ind = 0
character_count = {base:0 for base in ['A', 'T', 'C', 'G']}
# print(last_col_file.read()[:500])
# CAAAAAAAAAAAACAATAAAAAATAACAAACAACCACAAAAAAAAGATACAATACAAAAACAAAAAAAAACAAAAAAAAATAAACAAAAAAAACCAAAAA
# ACAAAAACTAAAAAAAAATAAAAAAAAAAAAACAACAAAAAAATGAAAAAAAAAACAAAAACAAAAAAAAAAAAAAAAAAATATAAACAAAAAAAAAAAA
# AAAAAAAAAAAATAAAAAACAAAAAAAAAAAAAAAAAAACAAAAACCAAAAAAAAAAAACCAAAACCAACAAGAAAAAACAAAAAAAAAAAAACAAAAAA
# CAAAAAACACACACCAATAAAAAAAAACACAACCCAAAAAACCATTACAAAAAACAAATACCACAAAAAAAAACAAAACAACAAAAACAAAAAAACAAAA
# CAAAAAAAAAAATAAAAACAAAATCAAAAACTAAACAAAAAAATTAAAAAAAAAAACCAAAAAAAAACAAAAAACCAACAAAAAAAACAAAACCAA
while(True):
    character = last_col_file.read(1)
    if(not character):
        break
    if(character!='$' and character!='\n'):
        last_col_arr[character].append(local_ind)
        character_count[character]+=1
        if(local_ind>0 and local_ind % delta == 0):
            for b in ['A', 'T', 'C', 'G']:
                rank_arr[b].append(character_count[b])
        local_ind+=1
    if local_ind >= 500:
        break
    

last_col_file.close()
print(last_col_arr['C'])
# find C at index 6

def rank(char, index, delta):
    if index % delta == 0:
        # return rank_arr[char][int(index/delta)]
        pass
    else:
        # return index % delta
        if index % delta > delta / 2:
            print('upper')
            print(index + (delta - (index % delta)))

        else:
            print('lower')
            print(index - (index % delta))


# print(rank('C', 20, delta))
# print(rank('C', 7, delta))
# print(rank('C', 9, delta))
# print(rank('C', 16, delta))