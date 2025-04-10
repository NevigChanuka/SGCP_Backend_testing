import pandas as pd

def new_word_adder():
    while True:
        print("")
        word = input("Word: ")


        if word == '0':
            break
        else:
            df = pd.read_parquet('vocab_data.parquet', engine='pyarrow')
            result1 = df[df["words"].astype(str).str.contains(word, case=False)]
            result2 = df[df["words"].astype(str) == word]

            with open('text.txt', 'r', encoding='utf-8') as file:
                content = file.read()

            words = content.split()
            matches = [word for word in words if word == word]

            if not result1.empty:
                print(result1)
            if not result2.empty:
                print(result2)
            if not matches:
                print(matches)



            if bool(result1.empty and result2.empty) and not bool(matches):
                with open('text.txt', 'a', encoding="utf-8") as file:
                    file.write(f'  {word}  ')

                print("****word added****\n")
            else:
                add_word = input("Add: ")

                if add_word == '1':
                    with open('text.txt', 'a', encoding="utf-8") as file:
                        file.write(f'  {word}  ')

                print("--------------------------------------------------")





new_word_adder()