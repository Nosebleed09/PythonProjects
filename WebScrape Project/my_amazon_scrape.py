import requests
from bs4 import BeautifulSoup
from datetime import datetime
# found headers details from amazon site, request headers
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
  'Accept-Language': 'en-IN,en-US;q=0.9,en;q=0.8'
}

def get_product_details(product_url: str) -> dict:  #a dict of product detials will be returned
# Get the product page content and create a soup
  page = requests.get(product_url, headers=headers)
  soup = BeautifulSoup(page.content, features='lxml')
  try:
    product_details={}
    
    title=soup.find("span", attrs={'id': 'productTitle'}).get_text().strip() 
    extracted_price = soup.find('span', attrs={'class': 'a-price'}).get_text().strip()
    price = '$' + extracted_price.split('₹')[1] #splitting the text based on rupee and then selecting the second element ['$','456']
  # price = soup.find('span', attrs={'class': 'a-price'}).get_text().strip()
  
    product_details['title']=title
    product_details['price']=price
    product_details['product_url'] = product_url
    return product_details
  except Exception as error:
    print(f"Product couldnt be found. Exited with error: {error}")


def records_for_product(product_name,product_det:dict):
  current_log=datetime.now()
  file='productname.txt'
  try:
    with open(product_name, "x") as file:
        file.write(f"NEW RECORD at {current_log.strftime("%D-%m-%Y"),current_log.strftime("%H:%M:%S")}\n")
        for k,y in product_det:
          file.write(f"{k}-->{y}\n")
        
  except FileExistsError:
    print(f"File '{product_name}' already exists.")
    
    with open(product_name, "a") as file:
        file.write(f"NEW RECORD at {current_log.strftime("%D-%m-%Y"),current_log.strftime("%H:%M:%S")}\n")
        for k,y in product_det.items():
          file.write(f"{k}-->{y}\n")



product_name=input("Enter product name or tag ")
product_url=input("ENter URL of product")
# myurl='https://www.amazon.in/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/9355421982/?_encoding=UTF8&pd_rd_w=v0bkD&content-id=amzn1.sym.823970d5-6634-49a2-a58c-62b0add430d7%3Aamzn1.symc.9b8fba90-e74e-4690-b98f-edc36fe735a6&pf_rd_p=823970d5-6634-49a2-a58c-62b0add430d7&pf_rd_r=27ZQ5Q6R4T018FRDFRAJ&pd_rd_wg=91k6O&pd_rd_r=997a0f07-f284-415f-95d7-91737fe46c4d&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d'
myproduct=get_product_details(product_url)
print(myproduct)
records_for_product(product_name,myproduct)

