import random

maxfiy_raqam = random.randint(1, 10)
tahminlar = 0

print("Assalomu alaykum! Raqamni toping o'yiniga xush kelibsiz!")
print("Men 1 dan 10 gacha bir raqam o'yladim. Uni toping!")

for urinish in range(3):
    taxmin = int(input("Raqamni kiriting (1 dan 10 gacha): "))
    tahminlar += 1

    if taxmin == maxfiy_raqam:
        print(f"Tabriklaymiz! Siz {tahminlar} urinishdagi raqamni topdingiz!")
        break
    elif taxmin < maxfiy_raqam:
        print("Yashirin raqam kattaroq!")
    else:
        print("Yashirin raqam kichikroq!")

else:
    print("Sizda urinishlar tugab ketdi! To'g'ri raqamni topolmadingiz.")

print("O'yin tugadi!")