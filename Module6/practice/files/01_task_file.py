with open("data/limericks.txt", "r", encoding="utf-8") as f:
    str_text = f.read()
    cnt_symb = str_text.replace(" ", "")
    cnt_symb = cnt_symb.replace("\n", "")
    cnt_symb = cnt_symb.replace("\t", "")
    f.seek(0)
    print(f.read())
    print("количество непробельный символов:", len(cnt_symb))

    cnt_lyr = str_text.count("\n\n")
    print("количество стихотворений:", cnt_lyr + 1)
