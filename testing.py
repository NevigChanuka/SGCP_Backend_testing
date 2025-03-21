import pandas as pd

# #
# column_name = input("coloumn: ")
#
# vocab_relation_df = pd.read_parquet('relation_table.parquet', engine='pyarrow')
# count = (vocab_relation_df[column_name] >= 0).sum()
# print(f'positive_count: {count}')
#
# vocab_feature_df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')
#
# number = [item for item in column_name if item.isdigit()]
# feature_table_row_index= int(''.join(number))
#
# print(feature_table_row_index)
# print(vocab_feature_df.iloc[feature_table_row_index])
# # vocab_relation_df.iloc[column_name, 0] = -1
#

vocab_feature_df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')

rows_with_minus_one = vocab_feature_df.index[vocab_feature_df['C0'] == -1].tolist()

row = []
# Print row numbers
print(rows_with_minus_one)
print(len(rows_with_minus_one))
print(len(row))