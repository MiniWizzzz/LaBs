import json
import os

# два пути для самурая
en_ru_path = os.path.join(os.getcwd(), "en_ru.txt")
ru_en_path = os.path.join(os.getcwd(), "ru_en.txt")

en_dictionary = {}
ru_dictionary = {}

try:
     with open(en_ru_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            (eng_w_str, ru_w_str) = line.split(" - ")
            ru_words = ru_w_str.replace("\n", "").split(", ")
            en_dictionary[eng_w_str] = ru_words

            for rw in ru_words:
                if rw in ru_dictionary:
                    ru_dictionary[rw].append(eng_w_str)
                else:
                    ru_dictionary[rw] = [eng_w_str]

     with open(ru_en_path, "w+", encoding="utf-8") as f:
         for ru_w, eng_w in sorted(ru_dictionary.items()):
                f.write(f"{ru_w} - {', '.join(eng_w)}\n")

except OSError:
    print("Проблемные проблемочки с файлом")