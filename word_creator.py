import re
import pandas as pd
from pandas.io.sas.sas_constants import encoding_length

def feature_creator():

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

    # write features into list and sava
    for feature in features_list:
        get_user_input = input(feature + ": ")

        if get_user_input == "1":
            binary_feature_rows[0].append(1)
        else:
            binary_feature_rows[0].append(0)


    return binary_feature_rows

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
        f'R{column_num}': [word_raw_num],
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
        updated_df = pd.concat([existing_df, new_word], ignore_index=True).fillna(0)
        updated_df.to_parquet('vocab_data.parquet', engine='pyarrow', compression='none')
        # print(updated_df)

    except FileNotFoundError:
        new_word.to_parquet('vocab_data.parquet', engine='pyarrow', compression='none')
        # print(new_word)

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

        pd.read_parquet('vocab_feature.parquet', engine='pyarrow')

    finally:
        existing_df = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
        get_row_number = existing_df[existing_df['words'] == word].index[0]
        #print(get_row_number)



    return int(get_row_number)



def feature_table_creator():

    # Check file exists
    try:

        existing_df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')

        rows = feature_creator()

        new_data = pd.DataFrame(rows, columns=existing_df.columns)

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
        pass


        # data = feature_creator()
        # print(data)
        # new_data = pd.DataFrame(data)
        #
        # df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')
        # updated_df = pd.concat([df, new_data], ignore_index=True)
        #
        # raw_number = updated_df.index[-1]
        #
        # # print(updated_df)
        #
        # return raw_number



    # '0': ඒක වචන
    # '1': බහු වචන
    # '2': උක්තය
    # '3': අනුක්තය
    # '4': ප්‍රථම පුරුෂ
    # '5': උත්තම පුරුෂ
    # '6': මධ්‍යම පුරුෂ
    # '7': පුරුෂ ලිංග
    # '8': ස්ත්‍රී ලිංග
    # '9': නපුංසක ලිංග
    # '10': සර්ව නාම
    # '11': අනියමාර්ථ නාම
    # '12': පුද්ගල නාම
    # '13': ස්ථාන නාම
    # '14': ක්‍රියාපද
    # '15': නිපාත
    # '16': ක්‍රියා විශේෂණ
    # '17': නාම විශේෂණ















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
                relation_table_creator(raw_number, 0) # R0 = ක්‍රියාපද

            elif vocab_type == "2":
                raw_number = vocab_table_creator(word)
                relation_table_creator(raw_number, 1) # R1 = නිපාත

            elif vocab_type == "3":
                raw_number = vocab_table_creator(word)
                relation_table_creator(raw_number, 2) # R2 = ක්‍රියා විශේෂණ

            elif vocab_type == "4":
                raw_number = vocab_table_creator(word)
                relation_table_creator(raw_number, 3) # R3 = නාම විශේෂණ

            elif vocab_type =="5":
                raw_number = vocab_table_creator(word)
                column_num = feature_table_creator()
                relation_table_creator(raw_number, column_num)
                #print(column_num)
            else:
                print("Invalid Input")

                print('\nvocab_table\n')
                vocab_data_df = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
                print(vocab_data_df)

                print('\nrelation_table\n')
                relation_table_df = pd.read_parquet('relation_table.parquet', engine='pyarrow')
                print(relation_table_df)

                print('\nfeature_table\n')
                df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')
                print(df)








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



