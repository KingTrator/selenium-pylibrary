from selenium import webdriver
import os
import booking.constants as const
class Booking(webdriver.Chrome):  # inherits methods and attributes from webdriver.Chrome
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):  # override superclass method
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()  # imports a function from the superclass


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
