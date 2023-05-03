# ses_core.py>

import boto3
from botocore.exceptions import ClientError


def set_email_values():
    print("Please enter the email to send from:")
    print("example: no-reply@develop.keen-platform.com")
    SENDER = input()
    print()

    print("Please enter to to address:")
    print("example: brian.nipper@keends.com")
    RECIPIENT = input()
    print()

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    # CONFIGURATION_SET = "ConfigSet"

    AWS_REGION = "us-east-1"

    print("Please enter a subject line:")
    print("example: Hello from test messages")
    SUBJECT = input()
    print()

    # Use a simple message for quick spam validation
    print("Enter 1 for complex/HTML message or anything else for simple message")
    MSG_CODE = input()
    print()

    if MSG_CODE == "1":
        print("You input was for a complex/HTML message")

        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = (
            "Let's Reset\r\n"
            "Please click the button below to reset your password.\r\n"
            "https://keen-platform.com/auth/reset-password/NQ/bnjlmm-8be94fab7dc6d12e398d103ac21a33e1 \r\n"
            "Cheers,"
        )

        # The HTML body of the message.
        BODY_HTML = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="https://www.w3.org/1999/xhtml">
            <head>
                <title></title>
                <meta http–equiv="Content-Type" content="text/html; charset=UTF-8" />
                <meta http–equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0 " />
                <link href="https://fonts.googleapis.com/css?family=Montserrat:400,400i,700,700i" rel="stylesheet" />
                <style>
                @media only screen and (min–width:481px) and (max–width:699px) {{
                    .w_full {{
                        width: 100% !important;
                        }}
                    }}
                </style>
            </head>
            <body class="em_body" style="margin:0px; padding:0px; height: 100vh" bgcolor="#efefef;">
                <table class="w_full" align="center" width="700" border="0" cellpadding="0" cellspacing="0" style="width:700px; min-height:20%;" bgcolor="#186da4">
                    <tr>
                        <td align="center" valign="top" style="font-family:Montserrat, Arial, sans-serif; font-weight:600; font-size:4rem; line-height:60px; color:#ffffff; padding-top: 60px; padding-bottom: 40px;">Let&#x27;s Reset</td>
                    </tr>
                </table>
                <div class="w_full" style="width: 700px; background: #186da4; margin-left: auto; margin-right: auto; min-height:20%;">
                    <img src="https://files.keen-platform.com/email-template/reset.png" style="width: 20%; margin-left: auto; margin-right: auto; display: block;"  alt="Reset"/>
                </div>
                <table class="w_full" align="center" width="700" border="0" cellpadding="0" cellspacing="0" style="width:700px; min-height:40%;" bgcolor="#186da4">
                    <tr>
                        <td align="center" valign="top" style="font-family:Montserrat, Arial, sans-serif; font-size:1.3rem; line-height:2.5rem; color:#ffffff; padding: 10px; padding-bottom: 80px"><p>A reset link has been generated for you.</p></td>
                    </tr>
                    <tr>
                        <td align="center" valign="top">
                            <a href="https://keen-platform.com/auth/reset-password/NQ/bnjlmm-8be94fab7dc6d12e398d103ac21a33e1" style="background-color: #ffffff; border: none; border-radius: 5px; color: #186da4; font-family:Montserrat, Arial, sans-serif; font-weight:600; font-size:1.5rem; padding: 30px 60px; text-decoration: none;">Reset Keen Platform Password</a>
                        </td>
                    </tr>
                    <tr>
                        <td align="center" valign="top" style="font-family:Montserrat, Arial, sans-serif; font-size:1.3rem; line-height: 3rem; color:#ffffff; padding-top: 90px;">Your username is: {RECIPIENT}</td>
                    </tr>
                    <tr>
                        <td align="center" valign="top" style="font-family:Montserrat, Arial, sans-serif; font-size:1.3rem; line-height: 3rem; color:#ffffff; padding-top: 90px;">Cheers,</td>
                    </tr>
                </table>
                <div class="w_full" style="width: 700px; background: #186da4; margin-left: auto; margin-right: auto; min-height:20%;">
                    <img src="https://files.keen-platform.com/email-template/email_signature.png" style="width: 45%; margin-left: auto; margin-right: auto; display: block; padding-bottom: 60px;"  alt="The Keen Team"/>
                </div>
                <div class="w_full" style="width: 700px; background #EFEFEF; margin-left: auto; margin-right: auto; min-height: 20%;">
                    Headquarters | 700 Park Offices Dr. Ste. 150 | Research Triangle, NC 27709
                </div>
            </body>
        </html>
        """
    else:
        print("You input was for a simple message")
        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = (
            "Amazon SES Test (Python)\r\n"
            "This email was sent with Amazon SES using the "
            "AWS SDK for Python (Boto)."
        )

        # The HTML body of the email.
        BODY_HTML = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html>
            <head></head>
            <body>
                <h1>Amazon SES Test (SDK for Python)</h1>
                <p>This email was sent with <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the <a href='https://aws.amazon.com/sdk-for-python/'>AWS SDK for Python (Boto)</a>.</p>
            </body>
        </html>
        """

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client("ses", region_name=AWS_REGION)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                "ToAddresses": [
                    RECIPIENT,
                ],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": CHARSET,
                        "Data": BODY_HTML,
                    },
                    "Text": {
                        "Charset": CHARSET,
                        "Data": BODY_TEXT,
                    },
                },
                "Subject": {
                    "Charset": CHARSET,
                    "Data": SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response["Error"]["Message"])
        print()
    else:
        print("Email sent! Message ID:"),
        print(response["MessageId"])
        print()
