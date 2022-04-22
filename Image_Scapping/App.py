
import requests
from bs4 import BeautifulSoup
import os


#url = 'https://www.holidayhomes.com/s/search/53ebd367ef479?adword=hh_google%2Frowe%2Fkwd-297065173162%2Fck%3Ds%3Blc%3Dlt%3Bde%3Ddt%3Btc%3DROWE%3Bl%3Den%3Bok%3DHHom%3Bmk%3Db%3Bct%3D0%2Fin%2Fn-a%2F53ebd367ef479%2F453785009169%2Fholiday%20home%20manali&c=USD&gclid=EAIaIQobChMI9Nmul5Gn9wIVKMmUCR1vdwzXEAAYAiAAEgJ5rvD_BwE&hl=en_GB&mktasp=acid%3D1144720848%3Bcpid%3D10731579082%3Bagid%3D108935738787%3Badid%3D453785009169%3Bdvce%3Dc%3Bkwrd%3Dholiday%20home%20manali%3B'

def image_download(url,folder):
    try:
        os.makedirs(os.path.join(os.getcwd(),folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),folder))
    r  = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    #print(soup.title.text)
    images = soup.find_all('img')
    #print(images)
    i  = 0
    for image in images:
        #label = image['target']
        link =  image['src']
        with open('image_'+str(i)+'.jpeg','wb') as f:
            im  = requests.get(link)
            f.write(im.content)
        i = i+1


url = 'https://www.airbnb.co.in/s/Manali--Himachal-Pradesh/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Manali%2C%20Himachal%20Pradesh&place_id=ChIJP9A_FgiHBDkRzXZQvg6oKYE&checkin=2022-05-18&checkout=2022-05-25&adults=1&source=structured_search_input_header&search_type=autocomplete_click'
image_download(url,'images_folder')
