import generateHtmlPage
import json as jsonMod

if __name__ == '__main__':
	json = {}
	with open('content.json') as json_data:
		json = jsonMod.load(json_data)

	htmlContent = generateHtmlPage.topOfPage

	#bio description title
	htmlContent += generateHtmlPage.generateBioDescription(json['bioDescription'])

	#work content
	count = 0
	workArr = json['work']
	for w in workArr:
		if count % 2 == 0:
			htmlContent += generateHtmlPage.generateRightWork(w['link'], w['imageUrl'], w['title'], w['position'], w['location'], w['description'])
		else:
			htmlContent += generateHtmlPage.generateLeftWork(w['link'], w['imageUrl'], w['title'], w['position'], w['location'], w['description'])
		if 'article' in w:
			htmlContent += generateHtmlPage.generateArticle(w['article']['link'], w['article']['imageUrl'])
		if count == len(json['work']) - 1:
			htmlContent += '</div>'
		elif 'article' not in w:
			htmlContent += '<div class="row space"></div><div class="row space"></div>'
		count+=1
	
	#project content
	htmlContent += generateHtmlPage.topProject
	count = 0
	for p in json['projects']:
		if count % 2 == 0:
			htmlContent += generateHtmlPage.generateRightWork(p['link'], p['imageUrl'], p['title'], p['position'], '', p['description'])
		else:
			htmlContent += generateHtmlPage.generateLeftWork(p['link'], p['imageUrl'], p['title'], p['position'], '', p['description'])
		if count == len(json['projects']) - 1:
			htmlContent += '</div>'
		else:
			htmlContent += '<div class="row space"></div><div class="row space"></div>'
		count+=1

	#travel content
	htmlContent += generateHtmlPage.topTravel
	htmlContent += generateHtmlPage.generateTopTravel(json['travelDescription'], json['travelYoutube'])
	for p in json['photos']:
		htmlContent += generateHtmlPage.generateFancyImage(p['mainImage'], p['smallImage'], p['description'])

	#contact content
	htmlContent += generateHtmlPage.topContact
	htmlContent += generateHtmlPage.generateContactDescripion(json['contactDescription'])
	htmlContent += generateHtmlPage.generateBusinessCard()
	htmlContent += generateHtmlPage.bottomOfPage

	Html_file= open("index.html","w")
	Html_file.write(htmlContent)
	Html_file.close()
