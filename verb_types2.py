import pandas as pd

def letters_to_unicode(letters):
    return ' '.join(f"U+{ord(char):04X}" for char in letters)

def unicode_to_letters(unicode_string):
    try:
        # Split the input by spaces and convert each to a character
        letters = ''.join(chr(int(code[2:], 16)) for code in unicode_string)
        return letters
    except ValueError:
        return "Invalid Unicode input!"



# #print(unicode_list)
# print(letters_to_unicode('ලෙ'))












def relation_table_creator(verb_token, column_num):

    data = {
        f'R{column_num}': [verb_token],
    }

    verb_relation_data = pd.DataFrame(data)

    # Check file exists
    try:
        # Read from file
        verb_past_relation_df = pd.read_parquet('verb_past_relation_table.parquet', engine='pyarrow')
        updated_df = pd.concat([verb_past_relation_df, verb_relation_data], ignore_index=True).fillna(-1).astype(int)
        updated_df.to_parquet('verb_past_relation_table.parquet', engine='pyarrow', compression='none',index=False)
        # print(updated_df)

    except FileNotFoundError:
        verb_relation_data.to_parquet('verb_past_relation_table.parquet', engine='pyarrow', compression='none')
        # print(word_relation_data)

def duplicate_checker(existing_df, new_data):

    for index, row in existing_df.iterrows():
        print(new_data)
        print(row.values.tolist())

        if row.values.tolist() == new_data:
             return index


def word_type2(positive_numbers):

    global word
    verb_tokens = ''
    verb_feature_list =  []
    get_verify = ''



    for positive_number in positive_numbers:
        df = pd.read_parquet("vocab_data.parquet", columns=["words"])
        word = df.at[positive_number, "words"]
        unicode_list = letters_to_unicode(word).split()

        # List of Unicode characters to remove (in U+XXXX format)
        unicode_to_remove = ["U+0DCA", "U+0DD4", "U+0DD6", "U+0DD9", "U+0DDA", "U+0DDC", "U+0DDD", "U+0DDE", "U+0DD0",
                             "U+0DD1", "U+0DCF", 'U+0DD3']

        # Filter the list to remove the specified Unicode characters
        filtered_list = [char for char in unicode_list if char not in unicode_to_remove]
        verb_tokens = positive_number

        new_list = [[f"{filtered_list[0]} U+0DD0 {filtered_list[1]} U+0DD4"],  # බැලු
                    [f"{filtered_list[0]} U+0DD0 {filtered_list[1]} U+0DD3"],  # බැලී
                    [f"{filtered_list[0]} U+0DD0 {filtered_list[1]} U+0DD2"],  # බැලි
                    [f"{filtered_list[0]} U+0DD0 {filtered_list[1]} U+0DD6"],  # බැලූ
                    [f"{filtered_list[0]} U+0DD0 {filtered_list[1]} U+0DD9"],  # බැලෙ
                    [f"{filtered_list[0]} {filtered_list[1]} U+0DCF"],  # බලා
                    [f"{filtered_list[0]} U+0DD0 {filtered_list[1]} U+0DDA"],  # බැලේ
                    [f"{filtered_list[0]} U+0DD9 {filtered_list[1]} U+0DDA"],  # කෙරේ
                    [f"{filtered_list[0]} U+0DD0 {filtered_list[1]} U+0DCA"]  # කැව්
                    ]

        v1 = unicode_to_letters(new_list[0][0].split())
        v2 = unicode_to_letters(new_list[1][0].split())
        v3 = unicode_to_letters(new_list[2][0].split())
        v4 = unicode_to_letters(new_list[3][0].split())
        v5 = unicode_to_letters(new_list[4][0].split())
        v6 = unicode_to_letters(new_list[5][0].split())
        v7 = unicode_to_letters(new_list[6][0].split())
        v8 = unicode_to_letters(new_list[7][0].split())
        v9 = unicode_to_letters(new_list[8][0].split())

        last_list2 = [f'{v1}වේ ය',
                      f'{v1}වා ය',
                      f'{v1}ණේ ය',
                      f'{v1}වෝ ය',
                      f'{v1}වාහ',
                      f'{v1}වාහු ය',
                      f'{v1}වෙහු',
                      f'{v1}වෙමු',
                      f'{v1}ණු',
                      f'{v1}ණෝ ය',
                      f'{v1}ණාහ',
                      f'{v1}ණුහු',
                      f'{v1}ණෙහු',
                      f'{v1}ණුමු',
                      f'{v1}ණෙමු',
                      f'{v2} ය',
                      f'{v2}හි',
                      f'{v2}මි',
                      f'{v2}මු',
                      f'{v3}ණි',
                      f'{v3}ණිහි',
                      f'{v3}ණිමි',
                      f'{v4}හ',
                      f'{v4}හු',
                      f'{v5}යි',
                      f'{v5}ති',
                      f'{v5}හි',
                      f'{v5}මි',
                      f'{v5}හු',
                      f'{v5}මු',
                      f'{v6}',
                      f'{v6} ය',
                      f'{v7}',
                      f'{v8}',
                      f'{v9}',

                      ]

        for new_word in last_list2:
            print(f"{new_word}")

        get_verify = input('all are correct? (y/n) : ')

        if get_verify == 'y':

            try:
                print(verb_tokens)
                verb_feature_present_df = pd.read_parquet('verb_past_feature.parquet', engine='pyarrow')
                #
                # row = [1] * 35
                # new_data = pd.DataFrame([row])
                # updated_df = pd.concat([verb_feature_present_df, new_data], ignore_index=True)
                # updated_df.to_parquet('verb_feature_present.parquet', engine='pyarrow', compression='none')


                relation_table_creator(verb_tokens, 0)



            except FileNotFoundError:

                row = [1] * 35

                new_data = pd.DataFrame([row])

                new_data.to_parquet('verb_past_feature.parquet', engine='pyarrow', compression='none')
                relation_table_creator(verb_tokens, 0)

                # new_data = pd.read_parquet('verb_feature_present.parquet', engine='pyarrow')

                #print(new_data)


        elif get_verify == 'n':

            for new_word in last_list2:
                print(f"{new_word}")
                get_input = input(': ')

                if get_input == "1":
                    verb_feature_list.append(1)
                else:
                    verb_feature_list.append(0)

            verb_feature_past_df = pd.read_parquet('verb_past_feature.parquet', engine='pyarrow')

            row_number = duplicate_checker(verb_feature_past_df, verb_feature_list)

            if row_number is not None and row_number >= 0:
                relation_table_creator(verb_tokens, row_number)

            else:
                verb_feature_past_df = pd.read_parquet('verb_past_feature.parquet', engine='pyarrow')

                new_data = pd.DataFrame([verb_feature_list])

                updated_df = pd.concat([verb_feature_past_df, new_data], ignore_index=True)

                updated_df.to_parquet('verb_past_feature.parquet', engine='pyarrow', compression='none')

                raw_number = updated_df.index[-1]
                relation_table_creator(verb_tokens, raw_number)


        else:
            print('Invalid input')




def row_checker(vocab_feature_df):

    limit_num = 0

    for index, row in vocab_feature_df.iterrows():
        # print(row.values.tolist())

        if row.values.tolist()[14] == 1:
            df = pd.read_parquet("relation_table.parquet", columns=["R0"])
            positive_numbers = df["R0"][df["R0"] > 0].to_numpy().tolist()
            positive_numbers = [num for num in positive_numbers if num > limit_num]
            print(positive_numbers)
            # word_type1(positive_numbers)


        elif row.values.tolist()[18] == 1:
            df = pd.read_parquet("relation_table.parquet", columns=["R23"])
            positive_numbers = df["R23"][df["R23"] > 0].to_numpy().tolist()
            positive_numbers = [num for num in positive_numbers if num > limit_num]
            print(positive_numbers)
            word_type2(positive_numbers)


# word_type1([131])


vocab_feature_df = pd.read_parquet('vocab_feature.parquet', engine='pyarrow').astype(int)
row_checker(vocab_feature_df)















