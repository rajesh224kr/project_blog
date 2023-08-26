def init_chrome_driver(arguments=[], experimental_options={}):
    MAX_LOAD_DRIVER_ATTEMPTS = 10

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    for argument in arguments:
        chrome_options.add_argument(argument)
    for key, value in experimental_options.items():
        chrome_options.add_experimental_option(key, value)

    for loop_counter in range(1, MAX_LOAD_DRIVER_ATTEMPTS + 1):
        try:
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
            if driver is not None:
                return driver
        except WebDriverException as e:
            if loop_counter == MAX_LOAD_DRIVER_ATTEMPTS:
                raise e
            else:
                pass
arguments= ['--incognito','ignore-certificate-errors','allow-insecure-localhost','--start-maximized']
page_main = init_chrome_driver(arguments) 



class performance_country:
    def __init__(self):
        self.performance_country: str = None #character varying(4000) ,
        self.performance_state: str = None #character varying(60),
    def performance_country_cleanup(self):
        if self.performance_country is not None:
            self.performance_country = self.performance_country[:2]      
        self.performance_state: str = 'indai'
