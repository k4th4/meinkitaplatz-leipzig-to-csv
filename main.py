import lxml
import bs4
import pandas as pd


def main():
	data_list = []
	local_file_list = [
	        "download/Kivan - Elternportal.html",
	        "download/Kivan - Elternportal (1).html",
					"download/Kivan - Elternportal (2).html"]
	
	for url in local_file_list:						   
		page_source = open(url, 'r').read()
		soup = bs4.BeautifulSoup(page_source, 'lxml')
		results = soup.findAll('div', {"class": "well col-xs-12"})
		for result in results:
			einrichtungsname = result.find('span', {"class": "einrichtung-name"}).text.strip()
			try:
				adresse = result.find('div', {"class": "gallery-info-toggleable"}).find('p').text.strip().split('(')[0]
			except AttributeError:
				adresse = ''
			try:
				ansprechpartner = list(result.find('div', {"class": "gallery-info-toggleable"}).children)[6].strip()
			except AttributeError:
				ansprechpartner =''
			try:
				telefonnummer = result.find('div', {"class": "gallery-info-toggleable"}).find('a').text.strip()
			except AttributeError:
				telefonnummer = ''
			try: 
				traeger = result.find('div', {"class": "gallery-info-toggleable"}).find('p', {"class": "ng-star-inserted"}).text .strip()  
			except AttributeError:
				traeger = ''

			data_list.append(
	        {
	            'einrichtungsname': einrichtungsname,
	            'adresse': adresse,
	            'ansprechpartner':  ansprechpartner,
							'telefonnummer': telefonnummer,
	            'traeger':  traeger,
						
	        }
	    )
	
	df = pd.DataFrame(data_list)
	df.to_csv('kita_daten_uebersicht.csv', index=False)
		
if __name__ == "__main__":
	main()