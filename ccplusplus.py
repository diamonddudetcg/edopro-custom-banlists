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

additionalForbidden = [
		"There Can Be Only One"
		]
additionalLimited = []
additionalSemiLimited = []
additionalUnlimited = [
	"Diamond Dire Wolf",
	"Number S39: Utopia the Lightning", 
	"Gladiator Beast Augustus", 
	"Gladiator Beast Retiari", 
	"Gladiator Beast Gyzarus",
	"Test Panther",
	"Gladiator Beast Andabata",
	"Gladiator Beast Domitianus",
	"Koa'ki Meiru Urnight",
	"Shiranui Spectralsword",
	"Vision HERO Vyon",
	"Shiranui Shogunsaga",
	"Traptrix Myrmeleo",
	"Traptrix Dionaea",
	"Traptrix Mantis",
	"Ghostrick Alucard",
	"Brotherhood of the Fire Fist - Bear",
	"Predaplant Triphyoverutum",
	"Predaplant Chimerafflesia",
	"Shiranui Sunsaga",
	"Necrovalley Throne",
	"Wind-Up Zenmaines",
	"Heroic Challenger - Assault Halberd",
	"Evolzar Dolkka",
	"Gachi Gachi Gantetsu",
	"Number 101: Silent Honor ARK",
	"Master Hyperion",
	"The Agent of Miracles - Jupiter",
	"The Agent of Mystery - Earth",
	"The Agent of Life - Neptune",
	"The Executor of the Underworld - Pluto",
	"Protector of The Agents - Moon",
	"The Sacred Waters in the Sky",
	"Salamangreat Spinny",
	"Salamangreat Balelynx",
	"Salamangreat Circle",
	"Bujin Hiruko",
	"Bujin Hirume",
	"Bujin Mikazuchi",
	"Bujingi Peacock",
	"Bujin Yamato",
	"Bujingi Crow",
	"Bujingi Hare",
	"Bujin Arasuda",
	"Bujingi Quilin",
	"Bujingi Crane",
	"Bujintei Susanowo",
	"Bujintei Kagutsuchi",
	"Bujincarnation",
	"Springans Ship - Exblowrer",
	"Springans Merrymaker",
	"Springans Watch",
	"Great Sand Sea - Gold Golgonda",
	"Pacifis, the Phantasm City",
	"Phantasm Spiral Battle",
	"Marincess Blue Slug",
	"Marincess Coral Anemone",
	"U.A. Hyper Stadium",
	"Altergeist Meluseek",
	"Battlin' Boxer Lead Yoke",
	"Digital Bug Rhinosebus",
	"Impcantation Candoll",
	"Impcantation Chalislime",
	"Infinitrack Trencher",
	"Infinitrack Anchor Drill",
	"Infinitrack River Stormer",
	"Infinitrack Goliath",
	"Heavy Forward",
	"Koa'ki Meiru Maximus",
	"Koa'ki Meiru Wall",
	"Iron Core Specimen Lab",
	"Starlight Road",
	"Magical Musketeer Wild",
	"Magical Musketeer Calamity",
	"Magical Musketeer Starfire",
	"Magical Musketeer Kidbrave",
	"Magical Musketeer Doc",
	"Magical Musketeer Caspar",
	"Magical Musket - Steady Hands",
	"Magical Musket - Cross-Domination",
	"Magical Musket - Desperado",
	"Magical Musket - Dancing Needle",
	"Magical Musket - Fiendish Deal",
	"Magical Musket - Last Stand",
	"Gladiator Beast Noxious",
	"Megalith Ophiel",
	"Mermail Abyssleed",
	"Mermail Abyssmegalo",
	"Mermail Abyssteus",
	"Mermail Abyssturge",
	"Mermail Abysspike",
	"Mermail Abyssmander",
	"Mermail Abysslinde",
	"Mermail Abyssgunde",
	"Mermail Abyssgaios",
	"Mermail Abyssalacia",
	"Mermail Abysstrite",
	"Abyss-squall",
	"Abyss-sphere",
	"Myutant Arsenal",
	"Myutant Mist",
	"Myutant Beast",
	"Myutant ST-46",
	"Myutant M-05",
	"Myutant Synthesis",
	"Myutant Evolution Lab",
	"Predaplant Sarraceniant",
	"Predapruning",
	"Gladiator Rejection",
	"Abyss Shark",
	"Crystal Shark",
	"Double Fin Shark",
	"Valiant Shark Lancer",
	"Beautunaful Princess",
	"Silent Sea Nettle",
	"Bahamut Shark",
	"Number 37: Hope Woven Dragon Spider Shark",
	"Number 70: Malevolent Sin",
	"Number 47: Nightmare Shark",
	"Satellarknight Rigel",
	"Satellarknight Altair",
	"Satellarknight Sirius",
	"Satellarknight Deneb",
	"Satellarknight Alsahm",
	"Stellarknight Triverr",
	"Stellarknight Delteros",
	"Satellarknight Skybridge",
	"Tellarknight Genesis",
	"Stellarnova Alpha",
	"The Phantom Knights of Break Sword",
	"Time Thief Adjuster",
	"Time Thief Temporwhal",
	"Time Thief Double Barrel",
	"Time Thief Perpetua",
	"Thunder Dragonduo",
	"Thunder Dragondark",
	"Thunder Dragonroar",
	"Thunder Dragonhawk",
	"Thunder Dragon Thunderstormech",
	"Some Summer Summoner",
	"Batteryman Industrial Strength",
	"Batteryman Fuel Cell",
	"Vampire Voivode",
	"Vampire Vamp",
	"Vampire Duke",
	"Vampire Sorcerer",
	"Vampire Ghost",
	"Crimson Knight Vampire Bram",
	"Vampire Fascinator",
	"Vampire Takeover",
	"Wattgiraffe",
	"Watthydra",
	"Wattchimera",
	"Wattcastle",
	"Suanni, Fire of the Yang Zing",
	"Bi'an, Earth of the Yang Zing",
	"Bixi, Water of the Yang Zing",
	"Jiaotu, Darkness of the Yang Zing",
	"Pulao, Wind of the Yang Zing",
	"Chiwen, Light of the Yang Zing",
	"Yang Zing Path",
	"Yang Zing Creation",
	"Nine Pillars of Yang Zing",
	"Beat, Bladesman Fur Hire",
	"Filo, Messenger Fur Hire",
	"Folgo, Justice Fur Hire",
	"XX-Saber Gardestrike",
	"XX-Saber Garsem",
	"XX-Saber Emmersblade",
	"XX-Saber Darksoul",
	"XX-Saber Gottoms",
	"XX-Saber Hyunlei",
	"Saber Slash",
	"Gottoms' Second Call",
	"Saber Vault",
	"Saber Hole",
	"Karakuri Muso mdl 818 \"Haipa\"",
	"Karakuri Bushi mdl 6318 \"Muzanichiha\"",
	"Karakuri Ninja mdl 339 \"Sazank\"",
	"Karakuri Merchant mdl 177 \"Inashichi\"",
	"Karakuri Barrel mdl 96 \"Shinkuro\"",
	"Karakuri Shogun mdl 00 \"Burei\"",
	"Karakuri Super Shogun mdl 00N \"Bureibu\"",
	"Shiranui Squire"
	]

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
banlistFilename = 'banlist/cc++.lflist.conf'
siteFilename ='site/plus/banlist.md'

#Card arrays
siteCards = []
simpleCards = [] # List of all TCG legal cards for banlist generation
ocgCards = [] # List of all OCG exclusive cards for banlist generation.

def printAdditionalArrays():
	print("Did I misspell something?")
	print("Additional forbidden cards:")
	print(additionalForbidden)
	print("Additional limited cards:")
	print(additionalLimited)
	print("Additional semi-limited cards:")
	print(additionalSemiLimited)
	print("Additional unlimited cards:")
	print(additionalUnlimited)

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
	outfile.write("---\ntitle:  \"Common Charity++\"\n---")
	outfile.write("\n\n## Common Charity++ F&L list")
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
		outfile.write("#[CC++ Format]\n")
		outfile.write("!CC++ %s.%s\n\n" % (datetime.now().month, datetime.now().year))
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

				if not hasCommonPrint:
					banTcg = -1

				cardName = card.get(name)

				if cardName in additionalForbidden:
					banTcg = 0
					additionalForbidden.remove(cardName)
				if card.get(name) in additionalLimited:
					banTcg = 1
					additionalLimited.remove(cardName)
				if card.get(name) in additionalSemiLimited:
					banTcg = 2
					additionalSemiLimited.remove(cardName)
				if card.get(name) in additionalUnlimited:
					banTcg = 3
					additionalUnlimited.remove(cardName)

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
					ocgCards.append(simpleCard)
					siteCards.append(simpleCard)
generateArrays()
printBanlist()
printSite()
printAdditionalArrays()