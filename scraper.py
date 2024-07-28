import requests 
import os

from bs4 import BeautifulSoup
import json

SCRAPINGBEE_API_KEY ="WBYQ36VPKMI70A1HLQZ3BYZI43VTU0V241C9CBA90AOCSUJESBGNKM9XSHYN50PY3RKJVUVTDX1VA3U8"
scrapingbee_endpoint = 'https://app.scrapingbee.com/api/v1/'
login_url ='https://www.cicelysbeauty.com/my-account'

payload = {
    'username': 'shekina@idmacommerce.com',
    'password': 'kimyeonkoung10',
}
PROVIDED_COOKIES = """
sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.cicelysbeauty.com%2Fmy-account%2F; Domain=cicelysbeauty.com; Expires=Sun, 28 Jul 2024 02:12:55 GMT; Path=/, _ga_SN75ZLXP1G=GS1.1.1722130966.1.0.1722130975.0.0.0; Domain=cicelysbeauty.com; Expires=Mon, 01 Sep 2025 01:42:55 GMT; Path=/, wordpress_logged_in_96aae45b70c03f7c3a10c7d3a94febbe=sdcruz%7C1722303774%7C9Pje4K3P44zPzreAwtiicLrj7FhIXGlEAjnLXkA6oqj%7C0417104db03dc9080ca89663c43f95c13b46f4a3602115fd573411fb958d4f57; Domain=www.cicelysbeauty.com; Expires=Wed, 31 Dec 1969 23:59:59 GMT; HttpOnly; Path=/, _ga=GA1.1.959670499.1722130966; Domain=cicelysbeauty.com; Expires=Mon, 01 Sep 2025 01:42:55 GMT; Path=/, sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29
"""

def get_provided_cookie():
    js_scenario = {
        "instructions": [ 
            {
                "fill": [
                    "#username", payload['username']
                ]
            }, 
            {
                "fill": [
                    "#password", payload['password']
                ]
            },                    
            {
                "click": ".woocommerce-form-login__submit"
            },                    
            {
                "wait": 5000
            }
        ]
    }
    scrapingbee_response = requests.get(
        url='https://app.scrapingbee.com/api/v1/',
        params={
            'api_key': SCRAPINGBEE_API_KEY,
            'url': login_url, 
            'wait': '5000',
            'js_scenario': json.dumps(js_scenario)
        },
        
        
        
    )
    print('Response HTTP Status Code: ', scrapingbee_response.status_code)
    
    if scrapingbee_response.status_code == 200:
        print('Login successful!')

        PROVIDED_COOKIE = scrapingbee_response.headers.get('Set-Cookie')
        print(f" cookie header {PROVIDED_COOKIE}")
        return False, PROVIDED_COOKIE
    return True, None
       
def scrape_page_number(page: str, page_number: str):
    session = requests.Session()
      
    cookies_dict = {}
    for cookie in PROVIDED_COOKIES.strip().split(', '):
        parts = cookie.split(';', 1)
        if '=' in parts[0]:
            cookie_name, cookie_value = parts[0].split('=', 1)
            cookies_dict[cookie_name] = cookie_value
    session = requests.Session()
    # Set the cookies in the session
    for cookie_name, cookie_value in cookies_dict.items():
        print(f" cookie name {cookie_name}")
        session.cookies.set(cookie_name, cookie_value)

    # Define headers if needed
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = session.get(page, headers=headers)

    # Check if the request to the target page was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products_divs = soup.select('div.products.row.row-small.large-columns-5.medium-columns-3.small-columns-2.has-shadow.row-box-shadow-3-hover')

        urls = []
        # Extract href values from the divs
        for product_div in products_divs:
            image_zoom_divs = product_div.select('div.image-zoom_in a')
            for image_zoom_div in image_zoom_divs:
                href = image_zoom_div.get('href')
                if href:
                    urls.append({'url': href})
        """ start"""
        # Load existing data if the file exists
        output_file='extracted_urls.json'
        if os.path.exists(output_file):
            with open(output_file, 'r') as json_file:
                existing_urls = json.load(json_file)
        else:
            existing_urls = []

        page_key = page_number
        page_exists = False
        for page in existing_urls:
            if page['page_number'] == page_key:
                page_exists = True
                # Add new URLs to product_links if they do not already exist
                for url in urls:
                    if url not in page['products_links']:
                        page['products_links'].append(url)
                    break

        # If the page does not exist, add a new page with the product links
        if not page_exists:
            existing_urls.append({
                "page_number": page_key,
                "products_links": urls
            })

        # Save the updated data to the JSON file
        with open(output_file, 'w') as json_file:
            json.dump(existing_urls, json_file, indent=4)
        # Save the extracted URLs to a JSON file
        # with open('extracted_urls.json', 'w') as json_file:
        #     json.dump(urls, json_file, indent=4)
    else:
        print(f'Failed to retrieve the target page. Status code: {response.status_code}')

def scrape_product_page(page:str, page_name: str):
    session = requests.Session()
      
    cookies_dict = {}
    for cookie in PROVIDED_COOKIES.strip().split(', '):
        parts = cookie.split(';', 1)
        if '=' in parts[0]:
            cookie_name, cookie_value = parts[0].split('=', 1)
            cookies_dict[cookie_name] = cookie_value
    session = requests.Session()
    # Set the cookies in the session
    for cookie_name, cookie_value in cookies_dict.items():
        session.cookies.set(cookie_name, cookie_value)

    # Define headers if needed
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = session.get(page, headers=headers)

    # Check if the request to the target page was successful
    if response.status_code == 200:
        # Save the response content to a file
        with open('product_page_content.html', 'wb') as file:
            file.write(response.content)

        print('Authenticated page content saved to product_page_content.html')

        # Optionally, parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Initialize a list to hold the product information
        # Extract product details from the specified div
        product_info_div = soup.find('div', class_='product-info summary col-fit col entry-summary product-summary')

        product_title = product_info_div.find('h1', class_='product_title').get_text(strip=True) if product_info_div.find('h1', class_='product_title') else None
        reference_number = product_info_div.find('span', class_='stl_codenum').get_text(strip=True) if product_info_div.find('span', class_='stl_codenum') else None
        # case_pack = product_info_div.find('span', class_='stl_casepack').get_text(strip=True) if product_info_div.find('span', class_='stl_casepack') else None
        case_pack = soup.find('span', class_='stl_codenum_second').get_text(strip=True) if soup.find('span', class_='stl_codenum_second') else None
        image_address = soup.find('meta', property='og:image')['content'] if soup.find('meta', property='og:image') else None
        price = product_info_div.find('p', class_='price').get_text(strip=True) if product_info_div.find('p', class_='price') else None

        # Create a dictionary with the extracted details
        new_product = {
            'url': page,
            'Title': product_title,
            'Reference Number': reference_number,
            'Case Pack': case_pack,
            'Image Address': image_address,
            'Price': price
        }

        # Save the extracted information to a JSON file
        output_path = 'extracted_product_details.json'
        if os.path.exists(output_path):
            with open(output_path, 'r') as json_file:
                data = json.load(json_file)
        else:
            data = []
        # Check if the page already exists
        page_name = page_name
        page_exists = False

        for page in data:
            if page['page'] == page_name:
                page_exists = True
                # Check if the product already exists in contents
                if new_product not in page['contents']:
                    page['contents'].append(new_product)
                break

        # If the page does not exist, add a new page with the product
        if not page_exists:
            data.append({
                'page': page_name,
                'contents': [new_product]
            })

        # Save the updated information to the JSON file
        with open(output_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)      
    else:
        print(f'Failed to retrieve the target page. Status code: {response.status_code}')

def generate_pages():
    # Create a list to hold the page dictionaries
    pages = []

    # Loop through numbers from 1 to 55
    for i in range(1, 56):
        # Determine the page URL
        if i == 1:
            page_url = "https://www.cicelysbeauty.com/shop/"
        else:
            page_url = f"https://www.cicelysbeauty.com/shop/page/{i}"
        if "page" in page_url:
            page_number = f"page_{page_url.split('/')[-1]}"
        else:
            page_number = "page_1"
        # Create a dictionary for the current page
        page_dict = {
            "page": page_url,
            "page_number": page_number,
            "products_links": []
        }
        
        # Append the dictionary to the list
        pages.append(page_dict)

    # Save the list of dictionaries to a JSON file
    output_path = 'pages_list.json'
    with open(output_path, 'w') as json_file:
        json.dump(pages, json_file, indent=4)

if __name__ == '__main__':
    output_path = 'extracted_urls.json'
    if not os.path.exists(output_path):
        generate_pages()
        pages = None
        output_path = 'pages_list.json'
        with open(output_path, 'r') as file:
            pages = json.load(file)
        for page in pages:
            print(f" page {page}")
            scrape_page_number(page['page'],page['page_number'])
   
    # content = login_and_fetch_page()
    # parse_page(content)
    product_pages = None
    with open('extracted_urls.json', 'r') as file:
        product_pages = json.load(file)
    if product_pages:
        for product in product_pages:
            page_number = product['page_number']
            print(f" pag number {page_number}")

            for link in product['products_links']:
                print(f" url {link['url']}")
                scrape_product_page(link['url'],page_number)
