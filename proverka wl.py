class check():
    non_win = []
    win = []
    all_wallet = []


if __name__ == '__main__' :
    cheks = check()
    with open("Akkiwiningleam.txt") as win_list:
        win = [row.strip() for row in win_list]

    with open("moiakki.txt") as moi_acc:
        moi = [row.strip() for row in moi_acc]

    for i in win:
        cheks.all_wallet.append(i.lower())
    for i in moi:
        cheks.all_wallet.append(i.lower())


    for i in range(len(moi)):

        if cheks.all_wallet.count(moi[i].lower()) >= 2: cheks.win.append(moi[i].lower())
        else: cheks.non_win.append(moi[i].lower())

    print(cheks.win)
