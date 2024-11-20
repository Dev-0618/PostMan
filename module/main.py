import yagmail
import os
import json

# Check if user details are saved (for reusability)
def load_user_credentials():
    if os.path.exists("user_credentials.json"):
        with open("user_credentials.json", "r") as file:
            return json.load(file)
    return None

# Save user credentials for future use
def save_user_credentials(sender_email, sender_password):
    credentials = {
        "sender_email": sender_email,
        "sender_password": sender_password
    }
    with open("user_credentials.json", "w") as file:
        json.dump(credentials, file)

# Send email function
def send_email(target_email, sender_email, sender_password, spoofed_from, subject, body, name=None, is_high_priority=False, attachment=None):
    # Replace placeholder {{.FirstName}} with the actual name
    if name:
        body = body.replace("{{.FirstName}}", name)

    # Initialize Yagmail client
    yag = yagmail.SMTP(sender_email, sender_password)

    # Headers for custom 'From' address
    headers = {'From': spoofed_from}

    # Set the priority if required
    if is_high_priority:
        headers['X-Priority'] = '1'  # High priority

    try:
        # Send email with custom headers
        yag.send(to=target_email, subject=subject, contents=body, headers=headers, attachments=attachment)
        print(f"Email sent successfully to {target_email}!")
    except Exception as e:
        print(f"Failed to send email to {target_email}: {e}")

# Main function to interact with the user
def main():
    # Load saved credentials (if available)
    credentials = load_user_credentials()

    if credentials:
        sender_email = credentials["sender_email"]
        sender_password = credentials["sender_password"]
        print("Credentials loaded from saved file.")
    else:
        # First-time user: ask for credentials
        sender_email = input("Enter your email address: ")
        sender_password = input("Enter your email password (or app password): ")
        save_user_credentials(sender_email, sender_password)
        print("Credentials saved for future use.")

    # Ask for email priority
    is_high_priority = input("Do you want to mark this email as high priority? (y/n): ").lower() == 'y'

    # Ask for single or bulk email
    email_type = input("Do you want to send this email to a single person or bulk? (single/bulk): ").lower()

    if email_type == "single":
        target_email = input("Enter the recipient's email: ")
        recipient_name = input("Enter the recipient's name: ")
    elif email_type == "bulk":
        target_email = input("Enter the file path containing the email list (one email per line): ")
        name_file = input("Enter the file path containing names (one name per line, corresponding to emails): ")
        with open(target_email, "r") as email_file, open(name_file, "r") as name_file:
            bulk_emails = [line.strip() for line in email_file.readlines()]
            bulk_names = [line.strip() for line in name_file.readlines()]

    # Ask for subject option
    subject_choice = input("Choose subject option (1 for pre-made templates, 2 for custom): ")

    if subject_choice == "1":
        print("Choose a subject template:")
        print("1. Important Account Update")
        print("2. Account Disabled Notification")
        print("3. Bulletin Alert")
        print("4. Company Wide Update")
        print("5. Email Server Migration Issue")
        print("6. LinkedIn Invitation Reminder")
        subject_choice = input("Enter your choice (1 or 2): ")
        if subject_choice == "1":
            subject = "Important Account Update"
            body = """
            <html>
            <head>
                <title></title>
            </head>
            <body>
             <a style="margin-left:13.5pt;">Hello {{.FirstName}},</a>
             <a style="margin-left:13.5pt;">Please refer to the vital info I&#39;ve shared with you using Google Drive.&nbsp;</a>            
             <a style="margin-left:13.5pt;">Click <a href="{{.URL}}">https://google.com/drive/docs/file012345</a> and sign in to view details..</a>            
             <a style="margin-left:13.5pt;">&nbsp;</a>            
             <a style="margin-left:13.5pt;">Regards.</a>            
             <a style="margin-left:13.5pt;">&nbsp;</a>            
             <a style="margin-left:13.5pt;">CONFIDENTIALITY NOTICE:&nbsp; This e-mail and any transmitted files are private and confidential and are solely for the use of the recipient(s)&nbsp;to whom it is addressed.&nbsp; Any unauthorized review, use, disclosure, distribution or copying of this communication is strictly forbidden.&nbsp; If you have received this communication in error, please delete and immediately notify the sender via the e-mail return address.&nbsp; Thank you for your compliance.</a>            
             <a style="margin-left:13.5pt;">Please consider the environment before printing this e-mail.</a>            
             <a style="margin-left:13.5pt;">&nbsp;</a>            
             <a style="margin-left:13.7pt;"></a>            
             To know more about this issue, please click below.</a>
            </body>
            </html>
            """

        elif subject_choice == "2":
            subject = "Account Disabled Notification"
            body = """
            <html>
            <head>
                <title></title>
            </head>
            <body>
            <h1 style="box-sizing: border-box; margin: 20px 0px 10px; font-size: 36px; line-height: 1.1; color: rgb(68, 114, 196);"><span class="marker" style=""><samp style=""><font face="Helvetica Neue, Helvetica, Arial, sans-serif"><span style="font-weight: 500;">Spotify&nbsp;</span></font><strong style="font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-weight: 500;">&reg;</strong></sama></span></h1>            
             Attention {{.FirstName}}!</a>
             <o:a></o:a></a>
             Your Spotify has been disabled.<br />
            You&#39;ve placed your&nbsp;account under the risk of termination by not keeping the correct information. &nbsp;</a>
             Please verify your account as soon as possible.</a>
             Ready to check? Click <a href="{{.URL}}">here</a> to get back your account.</a>
             Inc.Spotify</a>
             </a>            
             To know more about this issue, please click below.</a>
            </body>
            </html>
            """

        elif subject_choice == "3":
            subject = "Bulletin Alert"
            body = """
            <html>
            <head>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            </head>
            <body>
            <h3>Bulletin Alert!!</h3>
            <h3>Attention {{.FirstName}} {{.LastName}}:</h3>
             Bulletin Headline: Crime Suspect</a>
             Sending Agency: Police</a>
             Bulletin Time: 18:47</a>
             Bulletin Case#: 11-04626</a>
             Bulletin Author: Leroy Jethro #8847</a>
             Sending User #: 2892</a>
             <a href="{{.URL}}">To view the full bulletin alert click here</a></a>
            <br>
             To unsubscribe from these emails click <a href="{{.URL}}">here</a></a>
            
             To know more about this issue, please click below.</a>
            </body>
            </html>
            """

        elif subject_choice == "4":
            subject = "Company Wide Update"
            body = """
            <html>
            <head>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            </head>
            <body style="background-color:#A9A9A9">
            <div class="container" >
            <div class="container" style="background-color:#FFF;">
                <br><br>
                 This email is being sent to all employees with a company email address. If someone on your team does not have an company email, please refer them to our intranet to read this and other company wide communications. If you have issues accessing our intranet, please use the attached instructions.</a>
                <h1>Breaking News</h1>
                <h3>What's been happening at our company?</h3>
                 We are very proud to talk about what has been happening at our company. There is so much going on to be proud of in multiple divisions and across the globe. But what makes this email more important aside from showing you what is going on in other departments is discussing how this will affect you.</a>
                 We want to make sure that no employee feels left out because we value you {{.FirstName}}.</a>
                 I'm sure you're eager to hear about what's going on at our company, so go ahead and click the link below to read about what's going on. We appreciate your time and continued dedication as an employee at our company.</a>
                 Thank you for taking the time to read this email and for all the contributions you've made to our company. Remember you are a valued employee here and we look forward to hearing from you in the future</a>
                <h4>Exciting News See Bottom</a></h4>
                <br><br><hr>
                 Best Regards:</a>
                 The news Team</a>
                 </a>
            </div>
            </div>
            </body>
            </html>
            
             To know more about this issue, please click below.</a>
            """

        elif subject_choice == "5":
            subject = "Email Server Migration Issue"
            body = """
            <html>
            <head>
            <title></title>
            </head>
            <body>
             Hello {{.FirstName}},</a>
             The IT Department was running an email server migration last night and encountered an error with several email accounts.
            Your account {{.Email}} happened to be one of them.</a>
             We attempted to resolve this problem and believe we have fixed it.</a>
             If your email has been working just fine, please let us know by going to this secure <a  >website</a> and validate your email address is working.</a>
            
             Thanks for your quick cooperation,</a>
             IT</a>
            
             To know more about this issue, please click below.</a>
            </body>
            </html>
            """

        elif subject_choice == "6":
            subject = "LinkedIn Invitation Reminder"
            body = """
            <html>
            <head>
            <title></title>
            <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" />
            </head>
            <body>
             &nbsp;</a>
            
            <h1 style="color: rgb(68, 114, 196);"><b>LinkedIn</b></h1>
            
            <h2 style="color: rgb(68, 114, 196);">REMINDER</h2>
            
             &nbsp;</a>
            
            <h3><b>Invitation reminders/:&nbsp;&nbsp;&nbsp; From&nbsp; &nbsp;<a href="{{.URL}}">Steve Donaghy</a></b></h3>
            
            <h3><b>There are a total of </b><strong><b>4</b><b> </b></strong><b>other messages awaiting your reply.&nbsp;&nbsp;<a href="{{.URL}}">Go to INBOX now</a>.</b></h3>
            
             <b>&nbsp;</b></a>
            
             <b>Don&rsquo;t want to receive email notifications? Login to your LinkedIn account to <a href="{{.URL}}">unsubscribe.</a><br />
            LinkedIn values your privacy and respect your settings.</b></a>
            <br><br> To know more about this issue, please click below.</a>
            </body>
            </html>
            """

        else:
            print("Invalid choice! Defaulting to a generic message.")
            subject = "Generic Notification"
            body = """
            <html>
            <body>
            <h1>Notification</h1>
             Dear {{.FirstName}},</a>
             We have an update for you. Please click below to know more:</a>
            </body>
            </html>
            """
    elif subject_option == "2":
        subject = input("Enter your custom subject: ")
        body = input("Enter your custom email body (plain text or HTML): ")

    # Ask if the user wants to embed a clickable link
    embed_link = input("Do you want to embed a clickable 'Click here' button in the email? (y/n): ").lower()
    if embed_link == 'y':
        link_url = input("Enter the URL you want to embed: ")
        body = body.replace("</body>", f"""
         Click <a href="{link_url}" target="_blank">here</a> to proceed.</a>
        </body>
        """)

    # Ask for file attachment
    add_attachment = input("Do you want to attach a file? (y/n): ").lower()
    attachment = None
    if add_attachment == 'y':
        attachment = input("Enter the full file path for the attachment: ")

    # Send email to single or bulk
    if email_type == "single":
        send_email(target_email, sender_email, sender_password, "spoofed_email@example.com", subject, body, recipient_name, is_high_priority, attachment)
    elif email_type == "bulk":
        for email, name in zip(bulk_emails, bulk_names):
            send_email(email, sender_email, sender_password, "spoofed_email@example.com", subject, body, name, is_high_priority, attachment)

if __name__ == "__main__":
    main()
