"""Ask BAG API for adres and purpose of object"""
import requests

def ask_bag_adress(bagid, bagGebruiksdoel):
    """Ask BAG API for adres and purpose of object"""
    #formulate dictionary to fill the return of the API request
    adres_dict = {'identificatie':"", 'straatnaam':"", 'huisnummer':"", 'huisletter':"", 'postcode':"", 'woonplaats':"", 'gebruiksdoel':""}
    #gebruiksdoel zit nog niet in de API, vandaar return of standaard tekst

    gebruiksdoel = bagGebruiksdoel
    #in case no return (404), return "Helaas niet gevonden" text
    returnText = "Helaas niet gevonden"
    try:
        #BagAPI
        #the API Key is compulsory with each request, hal+json is the only format possible in the return of the request
        headers = {
            'X-Api-Key': "3cdcb3b8-ea40-4e53-bb08-094fafaba7f5",
            'Accept': "application/hal+json"
            }
        #formulate URL to query the BAG API based on bag id
        url = "https://bag.basisregistraties.overheid.nl/api/v1/panden/" + str(bagid)
        #formulate the GET request
        response = requests.request("GET", url, headers=headers)
        #convert returned response from json to python list
        bagReturn = response.json()
        #fill the dictionary
        adres_dict["identificatie"] = bagReturn["identificatiecode"]

        #based on the linked "verblijfsobject" GET hoofdadres
        bagVerblijfUrl = bagReturn["_links"]["verblijfsobjecten"]["href"]
        response = requests.request("GET", bagVerblijfUrl, headers=headers)
        bagReturn = response.json()

        bagNummerUrl = bagReturn["_embedded"]["verblijfsobjecten"][0]["_links"]["hoofdadres"]["href"]
        response = requests.request("GET", bagNummerUrl, headers=headers)
        bagReturn = response.json()
        adres_dict["huisnummer"] = bagReturn["huisnummer"]
        #try huisletter in case no return fill huisletter with ""
        try:
            adres_dict["huisletter"] = bagReturn["huisletter"]
        except: # pylint: disable=bare-except
            adres_dict["huisletter"] = ""
        adres_dict["postcode"] = bagReturn["postcode"]

        #query linked openbareruimte voor de straatnaam
        bagOpenbarerUrl = bagReturn["_links"]["bijbehorendeOpenbareRuimte"]["href"]
        response = requests.request("GET", bagOpenbarerUrl, headers=headers)
        bagReturn = response.json()
        adres_dict["straatnaam"] = bagReturn["naam"]

        #query linked woonplaats voor de woonplaats
        bagWoonplUrl = bagReturn["_links"]["bijbehorendeWoonplaats"]["href"]
        response = requests.request("GET", bagWoonplUrl, headers=headers)
        bagReturn = response.json()
        adres_dict["woonplaats"] = bagReturn["naam"]

        #compose 2 address strings from the found address
        adres1 = adres_dict["straatnaam"] + " " + str(adres_dict["huisnummer"]) + adres_dict["huisletter"]
        adres2 = adres_dict["postcode"] + " " + adres_dict["woonplaats"]
    except: # pylint: disable=bare-except
        #return the exception text in case of failure
        adres1 = returnText
        adres2 = returnText
    return adres1, adres2, gebruiksdoel
