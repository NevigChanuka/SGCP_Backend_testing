import pandas as pd
import numpy as np
import re

from pandas import bdate_range

word_tokens = []
features_list = []
sentences = []
counter = 0
word_roots = []
error_list = []





sentence = 'මම  ලිපිය ති බලන්නෙමි මම බලන්නෙමි'


verb_last1 = ["යි",
              "ති",
              "මු",
              "මි",
              "හු",
              "හි",

              "වයි",
              "වති",
              "වමු",
              "වමි",
              "වහු",
              'වහි',

              'න්නෙමි',
              'න්නෙමු',
              'න්නෙහු',
              'න්නෙහි',

              'න්නේ ය',
              'න්නී ය',
              'න්නෝ ය',

              'ව',
              'නු',
              'නුව',

              'වමින්',
              'මින්',
              'න',
              'නවා',
              'න්න',
              'න්නට',
              'න්නාට',
              'ද්දී',

              'න්නේ',
              'න්නා',
              'න්නෝ',
              'න්නන්',
              'න්නනට',
              'න්නී',

              ]

# Load data files
vocab_data = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
relation_table = pd.read_parquet('relation_table.parquet', engine='pyarrow')
vocab_feature = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')
verb_present_relation_table = pd.read_parquet('verb_present_relation_table.parquet', engine='pyarrow')
verb_present_feature = pd.read_parquet('verb_present_feature.parquet', engine='pyarrow')

# convert letters to Unicode
def letters_to_unicode(letters):
    return ' '.join(f"U+{ord(char):04X}" for char in letters)

# convert Unicode to letters
def unicode_to_letters(unicode_string):
    try:
        # Split the input by spaces and convert each to a character
        letters = ''.join(chr(int(code[2:], 16)) for code in unicode_string)
        return letters
    except ValueError:
        return "Invalid Unicode input!"

# remove all non-sinhala characters
def word_prepro(sentence):

    # filter the only sinhala words
    sinhala_pattern = r'[\u200d\u0D80-\u0DFF]+'
    sentences = re.findall(sinhala_pattern, sentence)
    return [re.sub(r"\u200d", "", word) for word in sentences]

cleared_sentence = word_prepro(sentence)
correct_sentence = cleared_sentence

def feature_row_finder(filename, tokens):

    # read the file
    df = pd.read_parquet(filename, engine='pyarrow')
    # read the position of the word (x and y in the table)
    positions = np.argwhere(df.values == tokens)
    #print("relation table(x,y): ", positions)

    # filter the column no (y value)
    column_name = df.columns[positions[0][1]]
    number = [item for item in column_name if item.isdigit()]
    return int(''.join(number))



# token list creator
def words_to_tokens():

    print(cleared_sentence)

    for word in cleared_sentence:
        result = vocab_data[vocab_data['words'] == word]

        print(word)

        # if word not found
        if result.empty:

            found = False

            word_to_list = list(word)

            while word_to_list:
                word_to_list.pop()
                word =  ''.join(word_to_list)
                result = vocab_data[vocab_data['words'] == word]

                if not result.empty:
                    print("found: " + word)
                    word_roots.append(word)
                    word_tokens.append(result.index.tolist()[0])
                    found = True
                    break

            if not found:
                print("not found")
                word_roots.append(word)
                word_tokens.append(-1)


        else:
            print("found: " + word)
            word_roots.append(word)
            word_tokens.append(result.index.tolist()[0])

    print(word_roots)
    print(word_tokens)
    tokens_to_features()



def tokens_to_features():
    for token in word_tokens:

        if token != -1:

            feature_row = feature_row_finder('relation_table.parquet' , token)
            feature = vocab_feature.iloc[feature_row].astype(int)
            features_list.append(feature.tolist())

        else:
            features_list.append(-1)

    print(features_list)
    subject_finder(0)









# def final_output(correct_word, index):
#
#     cleared_sentence[index] = correct_word
#     cleaned_sent = ' '.join(cleared_sentence)
#     print(cleaned_sent)
#
#     # for index, value in enumerate(word_tokens):
#     #     if value == verb_token:
#     #         if cleared_sentence[index] == correct_word:
#     #             print("Correct!")
#     #             print(correct_word)
#     #
#     #         else:
#     #             print("Incorrect!")
#     #             print(correct_word)
#
#
# def get_feature_row(index):
#     filename = 'verb_present_relation_table.parquet'
#     feature_row = feature_row_finder(filename, word_tokens[index + 1])
#     vocab_feature_df = pd.read_parquet('verb_present_feature.parquet', engine='pyarrow')
#     features = vocab_feature_df.iloc[feature_row].astype(int)
#     feature_list = features.tolist()
#
#     return feature_list



# def verb_type_finder(verb_root, index, value):
#     if value == 1:
#         feature_row = get_feature_row(index)
#         if feature_row[3] == 1:
#             correct_verb = f'{verb_root}{verb_last1[3]}'
#             final_output(correct_verb, index + 1)
#             # print(correct_verb)
#
#     elif value == 2:
#         feature_row = get_feature_row(index)
#         if feature_row[2] == 1:
#
#             correct_verb = f'{verb_root}{verb_last1[2]}'
#             final_output(correct_verb, word_tokens[index + 1])
#             # print(correct_verb)


def verb_type_finder(verb_index, subject_index):
    verb_ends = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 30, 32, 33]


    for index, verb_end_part in enumerate(verb_last1):

        if cleared_sentence[verb_index] == f"{word_roots[verb_index]}{verb_end_part}":
            # print(f"{word_roots[verb_index]}{verb_end_part}")

            if index in verb_ends:
                sentences.append(subject_index)
                sentences.append(verb_index)
                sentences.append(word_roots[verb_index])
                sentences.append(f"{word_roots[verb_index]}{verb_end_part}")
                print(sentences)

                break

    if len(features_list) > verb_index + 1:
        # print(len(features_list) , verb_index + 1)
        subject_finder(verb_index + 1)







def verb_finder(subject_index):
    # print(features_list[subject_index + 1])
    verb_index = subject_index
    for row in features_list[subject_index + 1:]:

        verb_index += 1
        if row == -1:
            pass

        # ක්‍රියාපද-වර්තමාන
        elif row[14] == 1:
            verb_type_finder(verb_index, subject_index)
            break

        # ක්‍රියාපද-අතීත
        elif row[18] == 1:
            break











def verb_corrector(index_list):
    correct_verbs = []
    found = False
    for x in index_list:
        #correct_verbs.append(f"{sentences[2]}{verb_last1[x]}")
        # print(f"{sentences[2]}{verb_last1[x]}")

        if sentences[3] == f"{sentences[2]}{verb_last1[x]}":
            found = True
            break



    if not found:
        error_list.append(sentences[1])
        error_list.append(correct_verbs)

    sentences.clear()
    print(error_list)








def subject_finder(start_index):
    # print("start index: ", start_index)
    for index, row in enumerate(features_list[start_index:]):

        if row == -1:
            pass

        # උක්ත
        elif row[2] == 1:

            # ඒක වචන, උත්තම පුරුෂ
            if row[0] == 1 and row[5] == 1:
                print("ඒක වචන, උත්තම පුරුෂ")
                verb_finder(start_index + index)
                # verb_corrector([3])
                print(sentences)
                break

            # බහු වචන, උත්තම පුරුෂ
            elif row[1] == 1 and row[5] == 1:
                print("බහු වචන, උත්තම පුරුෂ")
                break


            #--------------------------------------------------------
            # ඒක වචන, ප්‍රථම පුරුෂ,
            elif row[0] == 1 and row[4] == 1:

                # පුරුෂ ලිංග
                if row[7] == 1:
                    pass
                    break

                #  ස්ත්‍රී ලිංග
                elif row[8] == 1:
                    pass
                    break


                # නපුංසක ලිංග
                elif row[9] == 1:
                    pass
                    break

            # බහු වචන, ප්‍රථම පුරුෂ,
            elif row[1] == 1 and row[4] == 1:

                # පුරුෂ ලිංග, ස්ත්‍රී ලිංග
                if row[7] == 1 and row[8] == 1:
                    pass
                    break

                # පුරුෂ ලිංග
                elif row[7] == 1:
                    pass
                    break

                #  ස්ත්‍රී ලිංග
                elif row[8] == 1:
                    pass

                # නපුංසක ලිංග
                elif row[9] == 1:
                    pass
            #--------------------------------------------------------
            # ඒක වචන, මධ්‍යම පුරුෂ,
            elif row[0] == 1 and row[6] == 1:

                # පුරුෂ ලිංග, ස්ත්‍රී ලිංග
                if row[7] == 1 and row[8] == 1:
                    pass

                # පුරුෂ ලිංග
                elif row[7] == 1:
                    pass

                #  ස්ත්‍රී ලිංග
                elif row[8] == 1:
                    pass

                # බහු වචන, මධ්‍යම පුරුෂ,
            elif row[0] == 1 and row[6] == 1:
                pass

                # පුරුෂ ලිංග, ස්ත්‍රී ලිංග
                if row[7] == 1 and row[8] == 1:
                    pass

        # අනුක්තය
        elif row[3] == 1:
            # print(row)
            pass

            # ඒක වචන, උත්තම පුරුෂ
            if row[0] == 1 and row[5] == 1:
                pass

            # බහු වචන, උත්තම පුරුෂ
            elif row[1] == 1 and row[5] == 1:
                pass


            #--------------------------------------------------------
            # ඒක වචන, ප්‍රථම පුරුෂ,
            elif row[0] == 1 and row[4] == 1:

                # පුරුෂ ලිංග
                if row[7] == 1:
                    pass

                #  ස්ත්‍රී ලිංග
                elif row[8] == 1:
                    pass

                # නපුංසක ලිංග
                elif row[9] == 1:
                    pass

            # බහු වචන, ප්‍රථම පුරුෂ,
            elif row[0] == 1 and row[4] == 1:
                pass

                # පුරුෂ ලිංග, ස්ත්‍රී ලිංග
                if row[7] == 1 and row[8] == 1:
                    pass

                # පුරුෂ ලිංග
                elif row[7] == 1:
                    pass

                #  ස්ත්‍රී ලිංග
                elif row[8] == 1:
                    pass

                # නපුංසක ලිංග
                elif row[9] == 1:
                    pass
            #--------------------------------------------------------
            # ඒක වචන, මධ්‍යම පුරුෂ,
            elif row[0] == 1 and row[6] == 1:

                # පුරුෂ ලිංග, ස්ත්‍රී ලිංග
                if row[7] == 1 and row[8] == 1:
                    pass

                # පුරුෂ ලිංග
                if row[7] == 1:
                    pass

                #  ස්ත්‍රී ලිංග
                elif row[8] == 1:
                    pass

                # බහු වචන, මධ්‍යම පුරුෂ,
            elif row[0] == 1 and row[6] == 1:
                pass

                # පුරුෂ ලිංග, ස්ත්‍රී ලිංග
                if row[7] == 1 and row[8] == 1:
                    pass

                # පුරුෂ ලිංග
                if row[7] == 1:
                    pass

                #  ස්ත්‍රී ලිංග
                elif row[8] == 1:
                    pass



words_to_tokens()



























