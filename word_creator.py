import re
import pandas as pd
from pandas.io.sas.sas_constants import encoding_length

def feature_creator():

    binary_feature_rows = []
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

    # write features into list and sava
    for feature in features_list:
        get_user_input = input(feature + ": ")

        if get_user_input == "1":
            binary_feature_rows.append(1)
        else:
            binary_feature_rows.append(0)

    data = {
        'C0': [binary_feature_rows[0]],  # ඒක වචන
        'C1': [binary_feature_rows[1]],  # බහු වචන

        'C2': [binary_feature_rows[2]],  # උක්තය
        'C3': [binary_feature_rows[3]],  # අනුක්තය

        'C4': [binary_feature_rows[4]],  # ප්‍රථම පුරුෂ
        'C5': [binary_feature_rows[5]],  # උත්තම පුරුෂ
        'C6': [binary_feature_rows[6]],  # මධ්‍යම පුරුෂ

        'C7': [binary_feature_rows[7]],  # පුරුෂ ලිංග
        'C8': [binary_feature_rows[8]],  # ස්ත්‍රී ලිංග
        'C9': [binary_feature_rows[9]],  # නපුංසක ලිංග

        'C10': [binary_feature_rows[10]],  # සර්ව නාම
        'C11': [binary_feature_rows[11]],  # අනියමාර්ථ නාම
        'C12': [binary_feature_rows[12]],  # පුද්ගල නාම
        'C13': [binary_feature_rows[13]],  # ස්ථාන නාම

        'C14': [binary_feature_rows[14]],  #ක්‍රියාපද
        'C15': [binary_feature_rows[15]],  #නිපාත
        'C16': [binary_feature_rows[16]],  #ක්‍රියා විශේෂණ
        'C17': [binary_feature_rows[17]]   #නාම විශේෂණ
    }

    return data

def duplicate_checker(existing_df, new_data):

    for index, row in existing_df.iterrows():
        # print(new_data.iloc[0].tolist())
        # print(row.values.tolist())

        if row.values.tolist() == new_data.iloc[0].tolist():
             # print("work")
             return index
        else:
            pass# print("not work")



def relation_table_creator(word_raw_num, column_num):
    # print('\nrelation_table\n')
    data = {
        column_num: [word_raw_num],
    }

    word_relation_data = pd.DataFrame(data)

    # Check file exists
    try:
        # Read from file
        existing_df = pd.read_parquet('relation_table.parquet', engine='pyarrow')
        updated_df = pd.concat([existing_df, word_relation_data], ignore_index=True).fillna(-1).astype(int)
        updated_df.to_parquet('relation_table.parquet', engine='pyarrow', compression='none',index=False)
        # print(updated_df)

    except FileNotFoundError:
        word_relation_data.to_parquet('relation_table.parquet', engine='pyarrow', compression='none')
        # print(word_relation_data)




# this table containing all the vocabulary
def vocab_table_creator(word):
    # print('\nvocab_table\n')

    data = {
        'words': [word],
    }

    new_word = pd.DataFrame(data)

    # Check file exists
    try:
        # Read from file
        existing_df = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
        updated_df = pd.concat([existing_df, new_word], ignore_index=True)
        updated_df.to_parquet('vocab_data.parquet', engine='pyarrow', compression='none')
        # print(updated_df)

    except FileNotFoundError:
        new_word.to_parquet('vocab_data.parquet', engine='pyarrow', compression='none')
        # print(new_word)

    finally:
        existing_df = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
        get_row_number = existing_df[existing_df['words'] == word].index[0]
        #print(get_row_number)



    return int(get_row_number)



def feature_table_creator():

    # Check file exists
    try:

        existing_df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')

        data = feature_creator()


        new_data = pd.DataFrame(data)

        raw_number = duplicate_checker(existing_df, new_data)

        if raw_number is not None and raw_number >= 0:
            return raw_number

        else:

            updated_df = pd.concat([existing_df, new_data], ignore_index=True)

            updated_df.to_parquet('vocab_feature.parquet', engine='pyarrow', compression='none')

            df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')

            # print('\nfeature_table\n')
            # print(df)

            raw_number = df.index[-1]

            return raw_number





    except FileNotFoundError:
        rows = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        ]

        new_data = pd.DataFrame(rows,
                                columns=['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11',
                                         'C12', 'C13',
                                         'C14',
                                         'C15', 'C16','C17'])
        new_data.to_parquet('vocab_feature.parquet', engine='pyarrow', compression='none')

        saved_df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')

        data = feature_creator()

        new_data = pd.DataFrame(data)

        updated_df = pd.concat([saved_df, new_data], ignore_index=True)

        raw_number = updated_df.index[-1]

        # print(updated_df)

        return raw_number



    # 'C0': ඒක වචන
    # 'C1': බහු වචන
    # 'C2': උක්තය
    # 'C3': අනුක්තය
    # 'C4': ප්‍රථම පුරුෂ
    # 'C5': උත්තම පුරුෂ
    # 'C6': මධ්‍යම පුරුෂ
    # 'C7': පුරුෂ ලිංග
    # 'C8': ස්ත්‍රී ලිංග
    # 'C9': නපුංසක ලිංග
    # 'C10': සර්ව නාම
    # 'C11': අනියමාර්ථ නාම
    # 'C12': පුද්ගල නාම
    # 'C13': ස්ථාන නාම
    # 'C14': ක්‍රියාපද
    # 'C15': නිපාත
    # 'C16': ක්‍රියා විශේෂණ
    # 'C17': නාම විශේෂණ















def word_creator():

    with open("text.txt", "r", encoding="utf-8") as text_file:
        text = text_file.read()

        #print(text)

        sinhala_pattern = r'[\u200d\u0D80-\u0DFF]+'
        sentences = re.findall(sinhala_pattern, text)
        cleared_sentences = [re.sub(r"\u200d", "", word) for word in sentences]

        print(cleared_sentences)


        # tokenized each word
        for word in cleared_sentences:

            print("\n" + word + "\n")
            print("1.ක්‍රියාපද\n"
                  "2.නිපාත\n"
                  "3.ක්‍රියා විශේෂණ\n"
                  "4.නාම විශේෂණ\n"
                  "5.නාම පද\n")

            vocab_type = input(": ")

            if vocab_type == "1":
                raw_number = vocab_table_creator(word)
                relation_table_creator(raw_number, 'R0') # R0 = ක්‍රියාපද

            elif vocab_type == "2":
                raw_number = vocab_table_creator(word)
                relation_table_creator(raw_number, 'R1') # R1 = නිපාත

            elif vocab_type == "3":
                raw_number = vocab_table_creator(word)
                relation_table_creator(raw_number, 'R2') # R1 = ක්‍රියා විශේෂණ

            elif vocab_type == "4":
                raw_number = vocab_table_creator(word)
                relation_table_creator(raw_number, 'R3') # R1 = නාම විශේෂණ

            elif vocab_type =="5":
                raw_number = vocab_table_creator(word)
                column_num = feature_table_creator()
                relation_table_creator(raw_number, f'R{column_num}')
                #print(column_num)
            else:
                print("Invalid Input")
                df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')
                last_row_index = df.index[-1]
                print('\nfeature_table\n')
                print(df)
                print(last_row_index)


def new_word_adder():
    while True:
        word = input("Word: ")

        if word == '0':
            break
        else:
            df = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
            result = df[df["words"].astype(str).str.contains(word, case=False)]
            print(result)

        add_word = input("Add: ")

        if add_word == '':
            with open('text.txt', 'a', encoding="utf-8") as file:
                file.write(f'  {word}  ')

        print("---------------------------------------------------")



