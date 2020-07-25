from core import InstagramBot, followers, following, inter

def useBot(bot, slow_mode = True):
	bot = InstagramBot("uname", "pass")	
	bot.signIn()

	print("Takip edilenler alınıyor..")
	x = bot.getFollowing()
	print("\nTakipçiler alınıyor..")

	y = bot.getUserFollowers()
	a = bot.intersection(x,y)

	cikarilanlar = 0
	for i in following:
		if i not in followers:
			bot.unfUser(i, slow_mode)
			cikarilanlar += 1
		else:
			print(i," ile karşılıklı takipleşiliyor.")


if __name__ = "__main__":
	useBot(InstagramBot, True)



