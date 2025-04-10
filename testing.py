import pandas as pd



# # Load the Parquet file
# df = pd.read_parquet("vocab_feature.parquet")
#
# # Replace null (NaN) values in column 'C18' with 0
# df["C18"] = df["C18"].fillna(0)
#
# # Save the modified DataFrame back to a Parquet file
# df.to_parquet("vocab_feature.parquet", index=False)




# # Load the Parquet file
# df = pd.read_parquet("vocab_data.parquet")
#
# # Modify the value at row 130 in column 'words'
# df.at[132, "words"] = "ගැය"  # Replace with the desired value
#
# # Save the modified DataFrame back to a Parquet file
# df.to_parquet("vocab_data.parquet", index=False)
#















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

# vocab_feature_df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')
#
# rows_with_minus_one = vocab_feature_df.index[vocab_feature_df['C0'] == -1].tolist()
#
# row = []
# # Print row numbers
# print(rows_with_minus_one)
# print(len(rows_with_minus_one))
# print(len(row))


# def new_word_adder():
#     while True:
#         word = input("Word: ")
#
#         if word == '0':
#             break
#         else:
#             df = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
#             result = df[df["words"].astype(str).str.contains(word, case=False)]
#

            #result = df[df["words"].astype(str) == word]
            # print(result1)
#             print(result)
#
#         add_word = input("Add: ")
#
#         if add_word == '':
#             with open('text.txt', 'a', encoding="utf-8") as file:
#                 file.write(f'  {word}  ')
#
#         print("--------------------------------------------------")
# #-
# new_word_adder()





def letters_to_unicode(letters):
    return ' '.join(f"U+{ord(char):04X}" for char in letters)

word =  "පොත"

print(letters_to_unicode(word))

#
#
#
# def unicode_to_letters(unicode_string):
#     try:
#         # Split the input by spaces and convert each to a character
#         letters = ''.join(chr(int(code, 16)) for code in unicode_string.split())
#         return letters
#     except ValueError:
#         return "Invalid Unicode input!"
#
#
#
# user_input = input("Enter Unicode codes : ").replace("U+", "").strip()
# print(user_input)
# print(unicode_to_letters(user_input))

















# def unicode_to_letters(unicode_string):
#     try:
#         # Split the input by spaces and convert each to a character
#         letters = ''.join(chr(int(code, 16)) for code in unicode_string.split())
#         return letters
#     except ValueError:
#         return "Invalid Unicode input!"
#
# if __name__ ==
#     user_input = input("Enter Unicode codes (e.g., U+0DC0 U+0DBA U+0DD2): ").replace("U+", "").strip()
#     result = unicode_to_letters(user_input)
#     print("Converted Letters:", result)


# def unicode_to_letters(unicode_string):
#     try:
#         # Split the input by spaces and convert each to a character
#         letters = ''.join(chr(int(code, 16)) for code in unicode_string.split())
#         return letters
#     except ValueError:
#         return "Invalid Unicode input!"
#

#
# if __name__ == "__main__":
#     choice = input("Choose an option: (1) Unicode to Letters (2) Letters to Unicode: ")
#     if choice == "1":
#         user_input = input("Enter Unicode codes (e.g., U+0DC0 U+0DBA U+0DD2): ").replace("U+", "").strip()
#         result = unicode_to_letters(user_input)
#         print("Converted Letters:", result)
#     elif choice == "2":
#         user_input = input("Enter letters: ")
#         result = letters_to_unicode(user_input)
#         print("Unicode Codes:", result)
#     else:
#         print("Invalid choice!")

