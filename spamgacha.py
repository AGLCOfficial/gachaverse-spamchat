#Made by nullfact0r
#Copyright 2019

#Imports
import sys
import argparse
import urllib.request
import urllib.parse
import urllib.error

#Functions
def sendmessage(name,message,channel=1):
	try:
		dataname = urllib.parse.quote_plus(name)
		datamsg = urllib.parse.quote_plus(message)
		data = f"haircoloracc=272727&chatx={datamsg}&namex={dataname}&eyes=6&pupil2color=272727&haircoloralt=6B0F0F&levelnum=1&skincolor=FFF0E2&eyebrows=4&favunit=1&backhair=1&blush=5&fronthair=211&eye1color=912020&profilex=Oh%20snap%2C%20your%20getting%20raped%20by%20the%20AGLC%21%20Anti%20Gacha%20Life%20Council%20on%20top%21&hatcoloralt=D0FFFD&haircolorfade=6B0F0F&hat=0&othercoloralt=912020&pupil1color=272727&mouth=3&pupil=4&ponytail=1&secretx=POO&submitx=1&other=23&glassescolor=912020&channelx={channel}&rearhair=227&accessorycolor=912020&friendx=POO&relationship=30&hatcolor=30AAEE&eye2color=912020&othercolor=272727&trait=30&job=20&glassescoloralt=912020&accessory=0&haircolor=912020&accessorycoloralt=6B0F0F&ahoge=1"
		req = urllib.request.Request("http://gachaverse.com/dataverse/versesubmitchat2.php",data.encode("utf-8"))
		req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
		req.add_header("Pragma","no-cache")
		req.add_header("Accept","*/*")
		urllib.request.urlopen(req)
		return True
	except urllib.error.HTTPError:
		return False

def main():
	argparser = argparse.ArgumentParser(description="Spam the gachaverse chatroom",epilog="Made by Tiber Septim (nullfact0r) of The Anti Gacha Life Council")
	argparser.add_argument("-n","--name",required=True,help="In-chat username")
	argparser.add_argument("-m","--message",required=True,help="Message to spam")
	argparser.add_argument("-c","--channel",help="Which channel to send messages in")
	args = argparser.parse_args()
	print("Spamming chat...")
	running = True
	while running:
		try:
			running = sendmessage(args.name,args.message,channel=args.channel or 1)
		except KeyboardInterrupt:
			sys.exit(0)
	print("Server down")

#Main
if __name__ == "__main__":
	main()