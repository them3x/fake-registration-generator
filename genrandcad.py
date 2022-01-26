#encoding: utf-8
import requests
import random
import sys

class gen():

	def request(self, loc):

		url = "https://www.fakexy.com/fake-address-generator-"+loc
		header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
		html = requests.get(url, headers=header)

		return html.text



def show(loc):
	html = gen().request(loc).encode('UTF-8')

	street = html.split('<td>Street</td>')[1].split('<td>')[1].split('</td>')[0]
	city = html.split('<td>City/Town</td>')[1].split('<td>')[1].split('</td>')[0]
	region = html.split('<td>State/Province/Region</td>')[1].split('<td>')[1].split('</td>')[0]
	zip = html.split('<td>Zip/Postal Code</td>')[1].split('<td>')[1].split('</td>')[0]
	phone = html.split('<td>Phone Number</td>')[1].split('<td>')[1].split('</td>')[0]
	country = html.split('<td>Country</td>')[1].split('<td>')[1].split('</td>')[0]
	latitude = html.split('<td>Latitude</td>')[1].split('<td>')[1].split('</td>')[0]
	longitude = html.split('<td>Longitude</td>')[1].split('<td>')[1].split('</td>')[0]

	name = html.split('<td>Full Name</td>')[1].split('<td>')[1].split('</td>')[0]
	gender = html.split('<td>Gender</td>')[1].split('<td>')[1].split('</td>')[0]
	birthday = html.split('<td>Birthday</td>')[1].split('<td>')[1].split('</td>')[0]
	ssn = html.split('<td>Social Security Number</td>')[1].split('<td>')[1].split('</td>')[0]

	card_brand = html.split('<td>Credit card brand</td>')[1].split('<td>')[1].split('</td>')[0]
	card_number = html.split('<td>Credit card number</td>')[1].split('<td>')[1].split('</td>')[0]
	card_expire = html.split('<td>Expire</td>')[1].split('<td>')[1].split('</td>')[0]
	card_cvv = html.split('<td>CVV</td>')[1].split('<td>')[1].split('</td>')[0]


        print "--------------------------------------"
	print "Full Name:",name
        print "Gender:",gender
        print "Birthday:",birthday
        print "Social Security Number:",ssn
        print "Phone Number:",phone
	print "--------------------------------------"
        print "Credit card brand:",card_brand
        print "Credit card number:",card_number
        print "Expire:",card_expire
        print "CVV:",card_cvv
        print "--------------------------------------"
	print "Street:",street
	print "City/Town:",city
	print "State/Province/Region:",region
	print "Zip/Postal Code:",zip
	print "Country:",country
	print "Latitude:",latitude
	print "Longitude:",longitude
        print "--------------------------------------"



locations = ['ar','au','bd','be','br','ca','cn','cz','fr','de','gr','hu','in','id','ir','it','jp','my','mx','nl','ng','pe','ph','pl','pt','ro','ru','sa','sg','za','kr','es','se','th','tr','ug','ua','uk','us','vn']
try:
	loc = sys.argv[1]
	if loc not in locations:
		print "Avaliable locations:\n",locations,'\n\n'
		exit(0)
except:

	loc = random.choice(locations)



show(loc)
