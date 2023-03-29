import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class link_launcher:
    def __init__(self) -> None:
        pass

    def launch(self):
        language_list = ['ar-SA', 'bg-BG', 'cs-CZ', 'da-DK', 'de-DE', 'el-GR', 'en-US', 'es-ES', 'et-EE', 'fi-FI', 'fr-FR', 'he-IL',
                         'hr-HR', 'hu-HU', 'it-IT', 'ja-JP', 'ko-KR', 'lt-LT', 'lv-LV', 'nb-NO', 'nl-NL', 'pl-PL', 'pt-BR', 'pt-PT',
                         'ro-RO', 'ru-RU', 'sk-SK', 'sl-SI', 'sr-BA', 'sv-SE', 'th-TH', 'tr-TR', 'uk-UA', 'zh-CN', 'zh-HK', 'zh-TW']
        #language_list = ['ar-SA', 'lt-LT']
        for language in language_list:
            options_ = Options()
            options_.add_argument('--lang='+language)
            driver = webdriver.Chrome(options=options_)
            driver.maximize_window()
            driver.get("https://www.google.com/")
            time.sleep(5)
            url = driver.current_url
            url = url.replace("/", "_").replace("?",
                                                "_").replace(".", "_").replace("=", "_").replace(":", "_")
            fullname = language+'_'+url+'.png'
            driver.save_screenshot(os.path.join(os.getcwd(), fullname))

            driver.quit()


if __name__ == '__main__':
    launcher = link_launcher()
    launcher.launch()
