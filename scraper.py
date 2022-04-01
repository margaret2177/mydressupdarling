from requests_html import HTMLSession


class Scraper():

	def getHome(self):
		urls = ['https://dressupdarling.online','https://hajimetenogal.com']

		s=HTMLSession()
		datas = []
		for u in urls:
			r = s.get(u)
			rawTitle=u.split('//')[1].split('.')[0]
			if rawTitle == 'hajimetenogal':
				itemBanner= 'https://hajimetenogal.com/wp-content/uploads/2021/06/New-Project-39.jpg'
			elif rawTitle == 'dressupdarling':
			 	itemBanner = 'https://dressupdarling.online/wp-content/uploads/2021/06/New-Project-49.jpg'
			 # rawGenre = r.html.find('ul > li:nth-child(3) > a')
			 # genre=[]
			 # for g in rawGenre:
			 # 	gen = g.find('a>span').text
			 # 		genre.append(gen)
			data = {
				# 'title':title,
				'url':u,
				'path':rawTitle,
				'itemBanner':itemBanner,
				'itemThumb' : r.html.find('figure.wp-block-gallery img.alignleft',first=True).attrs['src'],
				'title' : r.html.find('header > h1.entry-title',first=True).text
				# 'genre': genre
			}
			datas.append(data)

		return datas;
			


	def getChapterCount(self,u):
		if(u == 'dressupdarling'):
			url = 'https://dressupdarling.online'
		elif(u =='hajimetenogal'):
			url = 'https://hajimetenogal.com'
		# url = 'https://dressupdarling.online'
		# url = 'https://hajimetenogal.com'

		s=HTMLSession()
		r=s.get(url)
		item ={}
		itemThumb = r.html.find('figure.wp-block-gallery img.alignleft',first=True).attrs['src']
		tableInfoRaw = r.html.find ('ul.list-group.list-group-flush>li.list-group-item');
		tableInfo={}
		rawInfo = []
		for i in tableInfoRaw:
			print(i.text.split(':')[0])
			# tableInfo[i.find('li>span.mlabel').text] = i.find('li>span>strong').text
			try:
				if i.text.split(':')[0] =='Description':
					rawInfo.append('')
				rawInfo.append(i.text.split(':')[0])
				rawInfo.append(i.text.split(':')[1])
			except Exception as e:
				tableInfo['Description']=i.text.split(':')[0];
				# rawInfo.append(i.text.split(':')[0])
				# if i.text.split(':')[0] == 'Description':
				# 	label = 'Description'
				# 	value =
					
				print(e)
			
		
		ra = len(rawInfo) // 2
		step = 2;
		for i in range(ra):
			tableInfo[rawInfo[i * step]]=rawInfo[i*step+1]
			

			# print(info)
		# print(tableInfo)
		


		chapterCount = []

		count = r.html.find('figure.wp-block-gallery  ul.su-posts > li.su-post')

		for i,c in enumerate(count):
			text = c.find('a',first=True)
			# print(text.text)
			chapterCount.append({'text':text.text,'url':u, 'c':i+1})
		itemThumb = itemThumb
		item['thumbnail']=itemThumb
		item['info']= tableInfo
		item['chapters']=chapterCount
		item['title'] =  r.html.find('header > h1.entry-title',first=True).text
		return item
		# print(chapterCount)

	def scrapedata(self, u,c):
		if u == 'dressupdarling':
			url = f'https://dressupdarling.online/manga/my-dress-up-darling-chapter-{c}'
			s=HTMLSession()
			r=s.get(url)
			print(r.status_code)

			chapterItems = []

			
			chapter = r.html.find('div.separator')
			
		
			if not chapter:
				item = r.html.find('div.wp-block-image>figure.aligncenter>img',first=True)
				# chapterItems.append(r.html.find('div.wp-block-image>figure.aligncenter>img').attrs['src'])
					
				chapterItems.append(item.attrs['src'])
			for  c in chapter:	
				item = c.find('img.aligncenter',first=True) 	
				chapterItems.append(item.attrs['src']);

			return chapterItems

		elif u == 'hajimetenogal':
			url1 = f'https://hajimetenogal.com/manga/hajimete-no-gal-chapter-{c}'
			url2 = f'https://hajimetenogal.com/manga/hajimete-no-gal-chapter-{c}-my-first-girlfriend-is-a-gal'
			url = url1 if int(c)<128 else url2
			s=HTMLSession()
			r=s.get(url)
			print(r.status_code)

			chapterItems = []

			sel1='div.separator'
			sel2='entry-content'
			sel = sel1 if int(c)<128 else sel2
			chapter = r.html.find(sel)
			
		
			if not chapter:
				item = r.html.find('figure.aligncenter>img',first=True)
				# chapterItems.append(r.html.find('div.wp-block-image>figure.aligncenter>img').attrs['src'])
					
				chapterItems.append(item.attrs['src'])
			for  c in chapter:	
				item = c.find('img.aligncenter',first=True) 	
				chapterItems.append(item.attrs['src']);
			
			print(chapterItems)
			return chapterItems

		
			


# qoutes = Scraper()

# qoutes.scrapedata('hajimetenogal','138')
# qoutes.getChapterCount()
# qoutes.getHome()


		