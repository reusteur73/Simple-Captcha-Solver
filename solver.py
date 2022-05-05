import pyautogui
from tqdm import tqdm
from termcolor import colored 

# Code by @reusteur73


captcha_len = 5

letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters[0] = "0",r"nums-letters\0.png"
letters[1] = "1",r"nums-letters\1.png"
letters[2] = "2",r"nums-letters\2.png"
letters[3] = "3",r"nums-letters\3.png"
letters[4] = "4",r"nums-letters\4.png"
letters[5] = "5",r"nums-letters\5.png"
letters[6] = "6",r"nums-letters\6.png"
letters[7] = "7",r"nums-letters\7.png"
letters[8] = "8",r"nums-letters\8.png"
letters[9] = "9",r"nums-letters\9.png"
letters[10] = "a",r"nums-letters\a.png"
letters[11] = "b",r"nums-letters\b.png"
letters[12] = "c",r"nums-letters\c.png"
letters[13] = "d",r"nums-letters\d.png"
letters[14] = "e",r"nums-letters\e.png"
letters[15] = "f",r"nums-letters\f.png"
letters[16] = "g",r"nums-letters\g.png"
letters[17] = "h",r"nums-letters\h.png"
letters[18] = "i",r"nums-letters\i.png"
letters[19] = "j",r"nums-letters\j.png"
letters[20] = "k",r"nums-letters\k.png"
letters[21] = "l",r"nums-letters\l.png"
letters[22] = "m",r"nums-letters\m.png"
letters[23] = "n",r"nums-letters\n.png"
letters[24] = "o",r"nums-letters\o.png"
letters[25] = "p",r"nums-letters\p.png"
letters[26] = "q",r"nums-letters\q.png"
letters[27] = "r",r"nums-letters\r.png"
letters[28] = "s",r"nums-letters\s.png"
letters[29] = "t",r"nums-letters\t.png"
letters[30] = "u",r"nums-letters\u.png"
letters[31] = "v",r"nums-letters\v.png"
letters[32] = "w",r"nums-letters\w.png"
letters[33] = "x",r"nums-letters\x.png"
letters[34] = "y",r"nums-letters\y.png"
letters[35] = "z",r"nums-letters\z.png"
letters[36] = "A",r"nums-letters\AA.png"
letters[37] = "B",r"nums-letters\BB.png"
letters[38] = "C",r"nums-letters\CC.png"
letters[39] = "D",r"nums-letters\DD.png"
letters[40] = "E",r"nums-letters\EE.png"
letters[41] = "F",r"nums-letters\FF.png"
letters[42] = "G",r"nums-letters\GG.png"
letters[43] = "H",r"nums-letters\HH.png"
letters[44] = "I",r"nums-letters\II.png"
letters[45] = "J",r"nums-letters\JJ.png"
letters[46] = "K",r"nums-letters\KK.png"
letters[47] = "L",r"nums-letters\LL.png"
letters[48] = "M",r"nums-letters\MM.png"
letters[49] = "N",r"nums-letters\NN.png"
letters[50] = "P",r"nums-letters\PP.png"
letters[51] = "Q",r"nums-letters\QQ.png"
letters[52] = "R",r"nums-letters\RR.png"
letters[53] = "S",r"nums-letters\SS.png"
letters[54] = "T",r"nums-letters\TT.png"
letters[55] = "U",r"nums-letters\UU.png"
letters[56] = "V",r"nums-letters\VV.png"
letters[57] = "W",r"nums-letters\WW.png"
letters[58] = "X",r"nums-letters\XX.png"
letters[59] = "Y",r"nums-letters\YY.png"
letters[60] = "Z",r"nums-letters\ZZ.png"

match = []
coords = []

# Check all letters
for i in tqdm(range(0,len(letters)), total=len(letters), desc="Checking for letters", unit="letters", colour="blue"):
    if len(match) < captcha_len:
        if pyautogui.locateCenterOnScreen(letters[i][1]) != None:
            x, y =  pyautogui.locateCenterOnScreen(letters[i][1])
            if x  != None:
                raw = str(i), x, letters[i][0]
                match.append(raw)
    else:
        break

if len(match) < captcha_len:
    print("Not enough letters found, maybe two letters are the same?")
    print("I recommand reload page where you found the captcha, and hope there are more unique letters") 


# Sort match by growing coords
for i in range(len(match)):
    for j in range(i+1, len(match)):
        if match[i][1] > match[j][1]:
            match[i], match[j] = match[j], match[i]


f = ''
for i in match:
    f += i[2]

print(colored('I guess captcha is : '+ f, 'yellow'))
