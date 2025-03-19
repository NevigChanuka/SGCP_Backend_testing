import pandas as pd
import numpy as np


def relation_table_creator(word_raw_num, column_num):

    data = {
        f'R{column_num}': [word_raw_num],
    }

    word_relation_data = pd.DataFrame(data)

    # Check file exists
    try:
        # Read from file
        existing_df = pd.read_parquet('relation_table.parquet', engine='pyarrow')
        updated_df = pd.concat([existing_df, word_relation_data], ignore_index=True).fillna(-1).astype(int)
        updated_df.to_parquet('relation_table.parquet', engine='pyarrow', compression='none',index=False)
        #print(updated_df)

    except FileNotFoundError:
        word_relation_data.to_parquet('relation_table.parquet', engine='pyarrow', compression='none')
        # print(word_relation_data)



def change_relation_table(row_index,positions,vocab_relation_df,word_token):


      # move relation table value
      #print(vocab_relation_df)
      vocab_relation_df.iloc[positions[0][0], positions[0][1]] = -1
      vocab_relation_df.to_parquet('relation_table.parquet', engine='pyarrow', compression='none')
      #print(vocab_relation_df)

      vocab_relation_df.loc[positions[0][0], f'R{row_index}'] = word_token
      vocab_relation_df.to_parquet('relation_table.parquet', engine='pyarrow', compression='none')
      #print(vocab_relation_df)


def duplicate_checker(existing_df, new_data_list):

      for index, row in existing_df.iterrows():
            #print(new_data_list[0])
            #print(row.values.tolist())
            #print('')

            if new_data_list[0] == row.values.tolist():
                  return index








word = input("word: ")


# find word token
vocab_data_df = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
df = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
result = df[df["words"].astype(str) == word].index
word_token =result.tolist()[0]
print("word token: ", word_token)

# find word token position in vocab relation table
vocab_relation_df = pd.read_parquet('relation_table.parquet', engine='pyarrow')
positions = np.argwhere(vocab_relation_df.values == word_token)
print("relation table(x,y): ",positions)

# get the column name of the word in vocab relation table
column_name = vocab_relation_df.columns[positions[0][1]]
print(column_name)
feature_table_row_index = int(list(column_name)[1:][0])


# get raw details in vocab feature table
vocab_feature_table = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')
feature_row = vocab_feature_table.iloc[positions[0][1]]
#print(feature_row)

print(f"ඒක වචන: {feature_row.iloc[0]}\n",
      f"බහු වචන: {feature_row.iloc[1]}\n",
      f"උක්තය: {feature_row.iloc[2]}\n",
      f"අනුක්තය: {feature_row.iloc[3]}\n",
      f"ප්‍රථම පුරුෂ: {feature_row.iloc[4]}\n",
      f"උත්තම පුරුෂ: {feature_row.iloc[5]}\n",
      f"මධ්‍යම පුරුෂ: {feature_row.iloc[6]}\n",
      f"පුරුෂ ලිංග: {feature_row.iloc[7]}\n",
      f"ස්ත්‍රී ලිංග: {feature_row.iloc[8]}\n",
      f"නපුංසක ලිංග: {feature_row.iloc[9]}\n",
      f"සර්ව නාම: {feature_row.iloc[10]}\n",
      f"අනියමාර්ථ නාම: {feature_row.iloc[11]}\n",
      f"පුද්ගල නාම: {feature_row.iloc[12]}\n",
      f"ස්ථාන නාම: {feature_row.iloc[13]}\n",
      f"ක්‍රියාපද: {feature_row.iloc[14]}\n",
      f"නිපාත: {feature_row.iloc[15]}\n",
      f"ක්‍රියා විශේෂණ: {feature_row.iloc[16]}\n",
      f"නාම විශේෂණ: {feature_row.iloc[17]}\n",)

binary_feature_rows = [[]]
features_list = [
      "ඒක වචන",
      "බහු වචන",

      "උක්තය",
      "අනුක්තය",

      "ප්‍රථම පුරුෂ",
      "උත්තම පුරුෂ",
      "මධ්‍යම පුරුෂ",

      "පුරුෂ ලිංග",
      "ස්ත්‍රී ලිංග",
      "නපුංසක ලිංග",

      "සර්ව නාම",
      "අනියමාර්ථ නාම",
      "පුද්ගල නාම",
      "ස්ථාන නාම",

      "ක්‍රියාපද",
      "නිපාත",
      "ක්‍රියා විශේෂණ",
      "නාම විශේෂණ",
]

#get new row data
for feature in features_list:
      print("")
      get_user_input = input(feature + ": ")

      if get_user_input == "1":
            binary_feature_rows[0].append(1)
      else:
            binary_feature_rows[0].append(0)

# check new row  exists
row_index = duplicate_checker(vocab_feature_table, binary_feature_rows)

#print(row_index)

print('before ', positions[0][0], positions[0][1])
print('after ', positions[0][0], f'R{row_index}')
print('word token: ', word_token)

# if new row not exists
if row_index is None:


      # checks other word tokens assign to column in vocab relation table

      # get count of only positive values in the column
      positive_count = (vocab_relation_df[column_name] >= 0).sum()
      #print(positive_count)

      if positive_count == 1:

            #vocab_feature_table.iloc[feature_table_row_index] = -1
            vocab_feature_table.iloc[feature_table_row_index] = binary_feature_rows[0]
            vocab_feature_table.to_parquet('vocab_feature.parquet', engine='pyarrow', compression='none')
            #print(vocab_feature_table)
      else:
            #print(binary_feature_rows)
            new_data = pd.DataFrame(binary_feature_rows, columns=vocab_feature_table.columns)
            vocab_feature_table = pd.concat([vocab_feature_table, new_data], ignore_index=True)
            vocab_feature_table.to_parquet('vocab_feature.parquet', engine='pyarrow', compression='none')
            #print(vocab_feature_table)
            row_number = vocab_feature_table.index[-1]
            #print(row_number)
            relation_table_creator(word_token,row_number)


else:
      change_relation_table(row_index, positions, vocab_relation_df, word_token)





















      # vocab_feature_table.to_parquet('vocab_feature.parquet', engine='pyarrow', compression='none')
      # vocab_feature_table = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')
      # feature_row = vocab_feature_table.iloc[positions[0][1]]
      # print(feature_row)


















# def get_columns_and_values(file_path):
#       # Read the Parquet file into a DataFrame
#       df = pd.read_parquet(file_path)
#
#       for column in df.columns:
#         print(f"Column Name: {column}")
#         print(df.columns.get_loc(column))
#         print(f"Values:\n{df[column]}")
#         print("-" * 50)
#
#
# # Usage
# file_path = 'your_file.parquet'
# get_columns_and_values("relation_table.parquet")


