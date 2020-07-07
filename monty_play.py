import random

#配列を使うと「num以外の0が入っている扉(はずれの扉)を開く(除外する)」でつむっぽい

count = 0
tmp = 0
#3つのドアを設定
door = [0 ,0 ,0]
#3つの中から1つに整数の1を入れる = 正解の扉を設定している
#0がはずれの扉で1が正解の扉
door[random.randint(0,2)] = 1
#回答者がドアを選ぶ(numっていうのが回答者の選ぶ番号)
num = random.randint(0,2)
answer = door[num]

#ドアの表示
print("---------------------------------------------------")
print("ゲームスタート")
print()
print("3つの扉があります")
print("〇 〇 〇")
while(1):
	num = int(input("1,2,3の内扉番号を指定してください : "))
	if num < 0 or num >3:
		print("入力された整数は無効です")
		print()
	else:
		break
print("回答者が選んだのは" + str(num) + "番目のドアです")

#numは配列の番号なので-1する
num -= 1
#bat2doorには、はずれの扉番号がリストで書くのされている
bat2door = [i for i, num in enumerate(door) if num == 0]

print()

#はずれのドアの片方を一つ消している：2が入っているっていうのは扉が開いている状態
#tmpには開けるドア番号を保存させとく
#こっちは回答者が間違えの扉を指定してた場合
if num in bat2door:
	for i in bat2door:
		if i != num:
			tmp = i
#こっちは回答者があってる扉を選んでた場合
else:
	tmp = bat2door[random.randint(0,1)]
#ここではずれの内の扉を一つ開けている：2は扉が開いている状態
door[tmp] = 2

print(str(tmp+1) + "番目のドアが開きました")
print()
print("扉を変更しますか？")
while(1):
	print("Yes : 1  No :  0  ")
	judge = int(input("your ansower : "))
	print()
	if judge == 1 or judge == 0:
		break
	else:
		print("入力された整数は無効です")


if judge == 1:
	print("扉を変更しませんでした")
	#ドアを変更しなかったバージョン。正解したらcount_nochangeに＋１している
	if answer == 1:
		count += 1
else:
	print("扉を変更しました")
	#ドアを変更しているバージョン。ここではドアの変更を行っている。
	for i in range(3):
		if i != num and i != tmp:
			num = i
			break
	answer = door[num]

	#正解したらcount_changeに＋１している
	if answer == 1:
		count += 1

#count_num += 1

if count == 1:
	print("正解しました！")
else:
	print("残念！不正解！")
	print("正解の扉は" + str(door.index(1) + 1) + "番目のドアでした")
#num以外の0が入っている扉(はずれの扉)を開く(除外する)
