import urllib.request, json, operator
from datetime import datetime
header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
			'AppleWebKit/537.11 (KHTML, like Gecko) '
			'Chrome/23.0.1271.64 Safari/537.11',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding': 'none',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive'}
url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
request = urllib.request.Request(url, None, header)

#Cards that aren't in YGOPRODECK but are legal. 
additionalLegalCards = [68933343,94331452,31826057,89774530]

#Cards that are listed as legal in YGOPRODECK but aren't
notLegalCards = []

#(C) is common, (SP) is Short Print, (SSP) is Super Short Print, (DNPR) is Duel Terminal common
legalRarities = ['(C)', '(SP)', '(SSP)', '(DNPR)']

#Banlist status
banned = 'Banned'
limited = 'Limited'
semi = 'Semi-Limited'

#YGOPRODECK API keys
data = 'data'
card_sets = 'card_sets'
banlist_info = 'banlist_info'
ban_tcg = 'ban_tcg'
rarity_code = 'set_rarity_code'
card_images = 'card_images'
cardType = 'type'

#Token stuff
token = 'Token'

#My keys
name = 'name'
cardId = 'id'
status = 'status'

#Filename for banlist file
banlistFilename = 'banlist/charity.lflist.conf'
siteFilename ='site/ccbanlist.md'

#Card arrays
siteCards = []
simpleCards = [] # List of all TCG legal cards for banlist generation
ocgCards = [] # List of all OCG exclusive cards for banlist generation.

def printCorrectAdditionalCards():
	print(additionalLegalCards)

def writeCardToBanlist(card, outfile):
	try:
		outfile.write("%d %d -- %s\n" % (card.get(cardId), card.get(status), card.get(name)))
	except TypeError:
		print(card)

def writeCardToSite(card, outfile):
	cardStatus = card.get(status)
	cardStatusAsText = "Unlimited"
	if (cardStatus == -1):
		cardStatusAsText = "Illegal"
	elif (cardStatus == 0):
		cardStatusAsText = "Forbidden"
	elif (cardStatus == 1):
		cardStatusAsText = "Limited"
	elif (cardStatus == 2):
		cardStatusAsText = "Semi-Limited"

	cardUrl = "https://db.ygoprodeck.com/card/?search=%s"%card.get(name).replace(" ", "%20").replace("&", "%26")

	outfile.write("\n| [%s](%s) | %s |"%(card.get(name), cardUrl, cardStatusAsText))

def writeCardsToSite(cards, outfile):
	for card in sorted(cards, key=operator.itemgetter('status')):
		writeCardToSite(card,outfile)

def writeHeader(outfile):
	outfile.write("---\ntitle:  \"Common Charity\"\n---")
	outfile.write("\n\n## Common Charity F&L list")
	outfile.write("\n\n| Card name | Status |")
	outfile.write("\n| :-- | :-- |")

def writeFooter(outfile):
	outfile.write("\n\n###### [Back home](index)")

def printSite():
	with open(siteFilename, 'w', encoding="'utf-8") as siteFile:
		writeHeader(siteFile)
		writeCardsToSite(siteCards, siteFile)
		writeFooter(siteFile)

def printBanlist():
	with open(banlistFilename, 'w', encoding="utf-8") as outfile:
		outfile.write("#[Common Charity Format]\n")
		outfile.write("!Common Charity %s.%s\n\n" % (datetime.now().month, datetime.now().year))
		outfile.write("\n#OCG Cards\n\n")
		for card in ocgCards:
			writeCardToBanlist(card, outfile)
		outfile.write("\n#Regular Banlist\n\n")
		for card in simpleCards:
			writeCardToBanlist(card, outfile)

def generateArrays():
	with urllib.request.urlopen(request) as url:
		cards = json.loads(url.read().decode()).get(data)
		for card in cards:
			if card.get(card_sets) != None:
				images = card.get(card_images)
				banInfo = card.get(banlist_info)
				banTcg = 3
				if (banInfo == None):
					banTcg = 3	
				if (banInfo != None):
					banlistStatus = banInfo.get(ban_tcg)
					if (banlistStatus == None):
						banTcg = 3
					if (banlistStatus == banned):
						banTcg = 0
					if (banlistStatus == limited):
						banTcg = 1
					if (banlistStatus == semi):
						banTcg = 2

				cardSets = card.get(card_sets)
				hasCommonPrint = False
				for printing in cardSets:
					if printing.get(rarity_code) in legalRarities:
						hasCommonPrint = True

				#Manually add the cards that don't have legal prints but should be legal
				if card.get(cardId) in additionalLegalCards:
					if hasCommonPrint: 
						additionalLegalCards.remove(card.get(cardId))
					if not hasCommonPrint:
						hasCommonPrint = True

				if not hasCommonPrint:
					banTcg = -1

				if card.get(cardId) in notLegalCards:
					banTcg = -1

				alreadyInSite = False
				for variant in images:
					simpleCard = {}
					simpleCard[name] = card.get(name)
					simpleCard[status] = banTcg
					simpleCard[cardId] = variant.get(cardId)
					if not alreadyInSite:
						siteCards.append(simpleCard)
						alreadyInSite = True
					if (banTcg<3):
						simpleCards.append(simpleCard)

			if (card.get(card_sets)) == None and card.get(cardType) != token:
				for variant in card.get(card_images):
					simpleCard = {}
					simpleCard[name] = card.get(name)
					simpleCard[status] = -1
					variantCardId = variant.get(cardId)
					simpleCard[cardId] = variantCardId
					willBeLegal = False
					if variantCardId in additionalLegalCards:
						willBeLegal = True
						simpleCard[status] = 3
					if not willBeLegal:
						ocgCards.append(simpleCard)

					siteCards.append(simpleCard)
generateArrays()
printBanlist()
printSite()
printCorrectAdditionalCards()