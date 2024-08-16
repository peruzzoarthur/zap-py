from django.http import JsonResponse, HttpRequest, HttpResponse
import requests
import json

def fetch_data(request: HttpRequest) -> HttpResponse:

    if request.method == "GET":
        print("getter")

    url = 'https://glue-api.zapimoveis.com.br/v2/listings?user=dfb535b1-c8b2-4daa-8b36-05c64daaf695&portal=ZAP&includeFields=search%28result%28listings%28listing%28contractType%2ClistingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%2Cpage%2Cfacets%2CfullUriFragments%2CsuperPremium%28search%28result%28listings%28listing%28contractType%2ClistingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%29&categoryPage=RESULT&developmentsSize=2&topoFixoSize=1&superPremiumSize=3&business=RENTAL&parentId=null&listingType=USED&priceMax=1400&addressCity=Pelotas&addressLocationId=BR%3ERio+Grande+do+Sul%3ENULL%3EPelotas&addressState=Rio+Grande+do+Sul&addressPointLat=-31.770008&addressPointLon=-52.331334&addressType=city&unitTypes=HOME&unitTypesV3=HOME&unitSubTypes=UnitSubType_NONE%2CTWO_STORY_HOUSE%2CSINGLE_STOREY_HOUSE%2CKITNET&usageTypes=RESIDENTIAL&size=15&page=1&ref=&images=webp&viewport=null&__zt=mtc%3Adeduplication2023'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.zapimoveis.com.br/',
        'x-domain': '.zapimoveis.com.br',
        'X-DeviceId': 'dfb535b1-c8b2-4daa-8b36-05c64daaf695',
        'Origin': 'https://www.zapimoveis.com.br',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
    }

    try:
        # Make the request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        # Check if response is already in JSON format
        try:
            json_data = response.json()
        except ValueError:
            return JsonResponse({'error': 'Response is not in JSON format'}, status=500)

        # Save JSON data to a file
        with open('response.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        # Return JSON data as response
        return JsonResponse(json_data)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
