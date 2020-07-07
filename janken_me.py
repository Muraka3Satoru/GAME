import random


hand_list = {1:"グー",2:"チョキ",3:"パー"}
def janken():
	g,t,p = 0,0,0
	rand_num = random.randint(0,90)

	while(1):
		hand = int(input("1:グー 2:チョキ 3:パー   : "))
		if hand == 1  or hand == 2 or hand == 3:
			break
		print()
		print("1,2,3のどれかを入力してください")

	print("ポン！")
	print()
	print("あなた：" + hand_list[hand])

	if rand_num <= 30:
		g = 1
		print("相手：グー")
	elif rand_num >30 and rand_num <=60:
		t = 1
		print("相手：チョキ")
	else:
		p = 1
		print("相手：パー")
	i_and_you = [hand,g,t,p]
	return i_and_you


print("じゃんけんスタート！")
print()
print("じゃんけん！")
while(1):
	hand = janken()

	print("-----------------------------------------------")
	if (hand[0] == 1 and hand[2] == 1) or (hand[0] == 2 and hand[3] == 1) or (hand[0] == 3 and hand[1] ==1):
		print("あなたの勝ち")
		break
	elif (hand[0] == 1 and hand[3] == 1) or (hand[0] == 2 and hand[1] == 1) or (hand[0] == 3 and hand[2] ==1):
		print("あなたの負け")
		break
	else:
		print("あいこで！")
		#janken()