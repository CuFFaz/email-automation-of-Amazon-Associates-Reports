#Login Creds


USERNAME = 'your.email-to-AmazonAssociates@email.com                #YOUR AMAZON LOGIN CREDS
PASSWORD = 'your-password-to-amazon-associates'                     #YOUR AMAZON LOGIN CREDS
waitTime = 0                                                        #Put value "3" when you're on potato-internet



email_list = ["sampleemail1@gmail.com, sampleemail2@agsindia.com"]  #EMAIL IDS OF SINGLE/MULTIPLE RECIPIENTS
email_ID = "your-gmail-ID@gmail.com"                                #YOUR GMAIL EMAIL ID
email_pass = "your-gmail-password"                                  #YOUR GMAIL PASSWORD
subject = "subject for email"                                       #EMAIL SUBJECT
filename = "IMG_001"                                                #FILENAME OF THE AMAZON-REPORT IMAGE /// I SUGGEST NOT TO CHANGE


html = """\
    <html>
    <head></head>
    <body>
        <p>
        
        Hey There!
        
        Please Type your Email body over here.
        
        For a new line just type <br> after the sentence.
        
        This down below is that report image grabbed from amazon.

        <br><br>
        <img src="cid:IMG_001.png"/>
        <br><br>

        Thanks & Regards stuff would be here.

        Im outtie :-)
        
        <br>
        </p>
    </body>
    </html>
    """

