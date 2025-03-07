import re
import json

#def write_to_json:

def word_creator():

    # Read existing JSON file
    with open("binary_features.json", "r", encoding="utf-8") as binary_features_file:
        binary_features_data = json.load(binary_features_file)

    with open("vocab.json", "r", encoding="utf-8") as vocab_file:
        vocab_data = json.load(vocab_file)
        counter = vocab_data["word_count"]

    features_list = ["උක්තය",
                     "අනුක්තය",
                     "ආඛ්‍යාතය",
                     "කෘදන්තය/නාම ක්‍රියා",

                     "ප්‍රථම පුරුෂ",
                     "උත්තම පුරුෂ",
                     "මධ්‍යම පුරුෂ",

                     "ඒක වචන",
                     "බහු වචන",

                     "පුරුෂ ලිංග",
                     "ස්ත්‍රී ලිංග",
                     "නපුංසක ලිංග",

                     "ක්‍රියාපද",
                     "නාම පද",
                     "නිපාත",

                     ]

    with open("text.txt", "r", encoding="utf-8") as text_file:
        text = text_file.read()

        #print(text)

        sinhala_pattern = r'[\u200d\u0D80-\u0DFF]+'
        sentences = re.findall(sinhala_pattern, text)
        cleared_sentences = [re.sub(r"\u200d", "", word) for word in sentences]

        print(cleared_sentences)

        # tokenized each word
        for word in cleared_sentences:

            binary_features_list = []
            counter += 1


            # Update vocab_data
            vocab_data["word_count"] = counter  # update word count
            vocab_data[counter] = word  # add new words

            # Write to file after updating
            with open("vocab.json", "w", encoding="utf-8") as vocab_file:
                json.dump(vocab_data, vocab_file, ensure_ascii=False, indent=4)



            # write features into list and sava
            for feature in features_list:
                get_user_input = input(feature + ": ")
                binary_features_list.append(get_user_input)


            print(binary_features_list)
            # Add a new key-value pair
            binary_features_data[counter] = binary_features_list

            # Write updated data back
            with open("binary_features.json", "w", encoding="utf-8") as binary_features_file:
                json.dump(binary_features_data, binary_features_file , indent=4)




# def verb_finder():
#     with open("text.txt", "r", encoding="utf-8") as text_file:
#         text = text_file.read()
#
#         filter_words = [
#             r'නවා',
#             r'යි',
#             r'මි',
#             r'මු',
#             r'ති',
#             r'වි',
#             r'හ',
#             r'න්න'
#             r'න්නේය',
#             r'න්නීය',
#             r'න්නෝය',
#             r'වාය',
#             r'වෝය',
#             r'මින්',
#             r'ව',
#             r'වයි',
#             r'වමි',
#             r'වති',
#             r'වහු',
#             r'වහි'
#         ]
#
#         pattern = '|'.join(filter_words)
#
#         sinhala_pattern = r'[\u200d\u0D80-\u0DFF]+'
#         sentence = re.findall(sinhala_pattern, text)
#
#         new_tokenized_sentence = [re.sub(r"\u200d", "", word) for word in sentence]
#
#         for word in new_tokenized_sentence:
#             if re.search(pattern, word):
#                 print(word)

        #filtered_sentences  = re.findall(filter_words, text)






