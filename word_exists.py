import pandas as pd

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

new_word_adder()