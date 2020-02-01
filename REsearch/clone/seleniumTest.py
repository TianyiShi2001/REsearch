from selenium.webdriver import Chrome
import time
postUrl = 'http://127.0.0.1:8000/upload/'
sel = Chrome()
sel.get(postUrl)
sel.find_element_by_xpath('//textarea[@name="mcs"]').send_keys('gagaccacaacggtttccctctagaaataattttgtttaactttaagaaggagatataccatggcacatatgagcggccgcgtcgactcgagcgagctcccggggggggttct')
time.sleep(0.2)
sel.find_element_by_xpath('//textarea[@name="goi"]').send_keys('CGATCTACCATCTACTCGCCCGGGATCTGTGAATGAGGAATTACCAGAAACCGAACCCGAAGATAATGATGAGTTGCCTGAAACAGAACCTGAAAGCGATTCCGATAAACCTACCGTAACCTCGAATAAAACAGAAAACCAAGTTGCTGATGAAGATTATGATTCATTCGACGATTTTGTGCCCAGTCAAACACACACAGCCTCCAAAATACCTGTAAAAAATAAACGAGCCAAAAAGTGCACTGTAGAATCTGATTCATCATCTTCGGATGATT')
sel.find_element_by_xpath('//button[@type="submit"]').click()

time.sleep(100000)
