tweetData=open('tweets.txt','a')
tweetData.close()
tweetData=open('tweets.txt','r')
tweetList=[]
for tweet in tweetData:
	tweetList.append(tweet.strip())

def printTweets():
	print()
	for tweet in tweetList:
		print(tweet)
	print()

def addTweets():
	tweet=''
	while not(0<len(tweet)<=140):
		tweet=input('Tweet away! ')
	tweetList.append(tweet)
	printTweets()
	quit()

def quit():
	tweetData=open('tweets.txt','w')
	for tweet in tweetList:
		tweetData.write(tweet+'\n')
	exit()

def main():
	choice=0
	while choice!=3:
		choice=input('1.Tweet\n2.See\n3.Quit\n>>>')
		if choice.isdigit():
			choice=int(float(choice))
		if choice==1:
			addTweets()
		elif choice==2:
			printTweets()
		elif choice==3:
			quit()

main()