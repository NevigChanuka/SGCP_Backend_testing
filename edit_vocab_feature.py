import pandas as pd

get_row_number = int(input("row number: "))

vocab_feature_table = pd.read_parquet('vocab_feature.parquet', engine='pyarrow')
feature_row = vocab_feature_table.iloc[get_row_number]
print(feature_row)

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



vocab_feature_table.loc[get_row_number] = binary_feature_rows[0]
vocab_feature_table.to_parquet('vocab_feature.parquet', engine='pyarrow', compression='none')


