import time
import smtplib
import logindata
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from PIL import Image
from PIL import Image, ImageEnhance


extension = ".png"

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome('/home/vivek/python_projects/amazon-automation-part1/chromedriver', chrome_options=options)
driver.get('https://affiliate-program.amazon.in/')
action = ActionChains(driver)

time.sleep(logindata.waitTime)

#getting element ID
signin_element = driver.find_element_by_xpath('//a[@href="/login"]')
signin_element.click()

#dumping email ID by xpath
email_element = driver.find_element_by_xpath("//*[@id='ap_email']")
email_element.send_keys(logindata.USERNAME)

#dummping the password by xpath
pass_element = driver.find_element_by_xpath("//*[@id='ap_password']")
pass_element.send_keys(logindata.PASSWORD)
pass_element.click()

#sign-in 
cont_element_2 = driver.find_element_by_id('signInSubmit')
cont_element_2.click()
time.sleep(logindata.waitTime)

#dropping down list
#drop_element = driver.find_element_by_xpath("//*[@id='nav-link-accountList']")
#action.move_to_element(drop_element).perform()

report_element = driver.find_element_by_xpath('//a[@href="/home/reports?ac-ms-src=summaryforthismonth"]')
report_element.click()
time.sleep(3)

#screenshot collector
driver.get_screenshot_as_file(logindata.filename + extension)
driver.quit()

new_filename = logindata.filename + extension
img = Image.open(new_filename)
  
# Setting the points for cropped image
left = 419
top = 217
right = 1486
bottom = 729
factor = 2.5
# Cropped image of above dimension
# (It will not change orginal image)
img = img.crop((left, top, right, bottom))

width , height = img.size

img = img.resize((int(width/1.5),int(height/1.5)))
enhancer = ImageEnhance.Sharpness(img)
img = enhancer.enhance(factor)

img = img.save(new_filename)


fromaddr = logindata.email_ID

for toaddr in logindata.email_list:
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = logindata.subject
    msg['From'] = fromaddr
    msg['To'] = toaddr
    # Record the MIME type of text/html.
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(MIMEText(logindata.html, 'html'))
    image_name = new_filename
    image_location = new_filename

    with open(image_location, "rb") as fp:
        img = MIMEImage(fp.read())
    img.add_header("Content-ID", "<{}>".format(image_name))
    msg.attach(img)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, logindata.email_pass)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(fromaddr, toaddr, msg.as_string())
    s.quit()

