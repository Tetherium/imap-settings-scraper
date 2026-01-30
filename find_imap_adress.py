# INPUT/OUTPUT FILES
INPUT_FILE = "INPUT.txt"  #Each domain should be listed separately. like: allmediax.de /line/ arrildcamping.dk ...
OUTPUT_FILE = "OUTPUT.txt"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def fetch_imap_settings_via_search(domain_list, output_file):
    driver = webdriver.Chrome() 
    driver.get("https://imapsettings.com/")

    with open(output_file, 'w') as outfile:
        for domain in domain_list:
            try:
                email_to_search = f"1@{domain}"
                search_input = driver.find_element(By.CSS_SELECTOR, 'input.form-control[name="email"]')
                search_input.clear()
                search_input.send_keys(email_to_search)

                find_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-dark.px-lg-5')
                find_button.click()

                sleep(3)  

                imap_server = driver.find_element(By.ID, 'IMAP-hostname').text.strip()
                imap_port = driver.find_element(By.ID, 'IMAP-port').text.strip()

                result = f"'{domain}': ('{imap_server}', '{imap_port}'),"
                print(result)
                outfile.write(result + '\n')

            except Exception as e:
                print(f"Error: {domain} not information {str(e)}")
                outfile.write(f"'{domain}': ('none', 'none'),\n")

            sleep(2) 

    driver.quit()

if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as infile:
        domain_list = [line.strip() for line in infile if line.strip()]
    fetch_imap_settings_via_search(domain_list, OUTPUT_FILE)
