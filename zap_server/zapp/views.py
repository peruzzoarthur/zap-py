from django.http import JsonResponse, HttpRequest, HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def fetch_data(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        print("received post")
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)

            # Extract the URL from the received data
            url = data.get('url')
            if not url:
                return JsonResponse({'error': 'URL parameter is required'}, status=400)

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

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request'}, status=400)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
