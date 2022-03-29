from requests_html import HTMLSession


class Scraper():

	def getChapterCount(self):
		url = 'https://dressupdarling.online'
		s=HTMLSession()
		r=s.get(url)

		chapterCount = []

		count = r.html.find('figure.wp-block-gallery  ul.su-posts > li.su-post ')

		for c in count:
			text = c.find('a',first=True)

			chapterCount.append({'text':text.text})

		return chapterCount

	def scrapedata(self, c):
		url = f'https://dressupdarling.online/manga/my-dress-up-darling-chapter-{c}'
		s=HTMLSession()
		r=s.get(url)
		print(r.status_code)

		chapterItems = []

		chapter = r.html.find('div.separator')
		
		# print(quotes)

		for  c in chapter:
			
			item = c.find('img.aligncenter',first=True)
			
			chapterItems.append(
				item.attrs['src']
				);

		return chapterItems
			


# qoutes = Scraper()

# qoutes.scrapedata('1')
# qoutes.getChapterCount()


		