import re
import pandas as pd

get_word =input( "word: ")

# row = [['වෘක්ෂ', 'රුක්', 'ගස්', 'තුරු']]
#
# synonym_data = pd.DataFrame(row)
# synonym_data.to_parquet('synonym_data.parquet', engine='pyarrow')
#
# synonym_data_table = pd.read_parquet('synonym_data.parquet', engine='pyarrow')
#
# print(synonym_data_table)



def word_prepro(text):
    # sinhala_pattern = r'[^\u200d\u0D80-\u0DFF]+'
    # word = re.sub(sinhala_pattern, "", text).split(" ")
    # cleared_word =re.sub(r"\u200d", "", word[0])

    sinhala_pattern = r'[\u200d\u0D80-\u0DFF]+'
    sentences = re.findall(sinhala_pattern, get_word)
    cleared_sentences = [re.sub(r"\u200d", "", word) for word in sentences]

    return cleared_sentences

def word_exists(word_list):
    # exist = False
    synonym_data_table = pd.read_parquet('synonym_data.parquet', engine='pyarrow')
    for word in word_list:
        result  = synonym_data_table.astype(str).apply(lambda col: col.str.contains(word, case=False, na=False)).any().any()
        # result = synonym_data_table[synonym_data_table["words"].astype(str) == word]
        #result = vocab_data_df[vocab_data_df["words"].astype(str).str.contains(word, case=False)]
        # print(result)
    #     if not result.empty:
    #         print("*********************")
    #         exist = True
    #         break
    #
    return result



word_list = word_prepro(get_word)
word_ex = word_exists(word_list)

print(word_list)

if not word_ex:

    synonym_data_table = pd.read_parquet('synonym_data.parquet', engine='pyarrow')
    row = [word_list]
    synonym_data = pd.DataFrame(row)
    synonym_data_table = pd.concat([synonym_data_table, synonym_data], ignore_index=True).astype(str)
    synonym_data_table.to_parquet('synonym_data.parquet', engine='pyarrow')

    # print(row)
    print(synonym_data_table)




else:
    print("word found")
    # get_eq_word = input("සමාන පදය: ")