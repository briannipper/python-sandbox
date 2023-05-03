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
            "Cheers,"
        )

        # HTML Placeholder Values
        header = "Let's Reset!"
        icon_url = "https://develop.files.keen-platform.com/email-template/reset.png"
        icon_alt = "Reset"
        detail = "A reset link has been generated for you."
        button_text = "Reset Keen Platform Password"
        user = RECIPIENT
        button_url = "https://keen-platform.com/auth/reset-password/NQ/bnjlmm-8be94fab7dc6d12e398d103ac21a33e1"
        signature_url = "https://develop.files.keen-platform.com/email-template/email_signature.png"

        # The HTML body of the message.
        BODY_HTML = f"""<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            </head>
            <body>
                <div style="background-color: #efefef; margin: 0">
                    <table
                        style="
                            font-family: Montserrat, Arial, sans-serif;
                            font-size: 14px;
                            color: #ffffff;
                            width: 98%;
                            max-width: 600px;
                            float: none;
                            margin: 0 auto;
                            background: #186da4;
                        "
                        border="0"
                        cellpadding="0"
                        cellspacing="0"
                        valign="top"
                        align="left"
                    >
                        <tbody>
                            <tr>
                                <td
                                    align="center"
                                    valign="top"
                                    style="
                                        font-family: Montserrat, Arial, sans-serif;
                                        font-weight: 600;
                                        font-size: 24px;
                                        line-height: 22px;
                                        padding-top: 30px;
                                        padding-bottom: 32px;
                                    "
                                >
                                    { header }
                                </td>
                            </tr>
                            <tr align="middle">
                                <td style="padding-top: 24px">
                                    <img src="{ icon_url }" height="50" alt="{ icon_alt }" />
                                </td>
                            </tr>
                            <tr>
                                <td
                                    align="center"
                                    valign="top"
                                    style="
                                        font-family: Montserrat, Arial, sans-serif;
                                        font-size: 18px;
                                        line-height: 22px;
                                        color: #ffffff;
                                        padding-top: 24px;
                                    "
                                >
                                    { detail }
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding-top: 24px">
                                    <table border="0" cellpadding="0" cellspacing="0">
                                        <tbody>
                                            <tr>
                                                <td
                                                    align="center"
                                                    style="
                                                        height: 38px;
                                                        padding: 7px 24px;
                                                        border-radius: 4px;
                                                        background-color: #ffffff;
                                                    "
                                                >
                                                    <a
                                                        id="activate-url"
                                                        href="{ button_url }"
                                                        style="text-decoration: none"
                                                    >
                                                        <span
                                                        style="
                                                            background-color: #ffffff;
                                                            border: none;
                                                            border-radius: 5px;
                                                            color: #186da4;
                                                            font-family: Montserrat, Arial, sans-serif;
                                                            font-weight: 600;
                                                            font-size: 14px;
                                                        "
                                                        >{ button_text }</span
                                                        >
                                                    </a>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td
                                                align="center"
                                                style="
                                                    font-family: Montserrat, Arial, sans-serif;
                                                    color: #ffffff;
                                                    padding-top: 24px;
                                                    font-size: 12px;
                                                "
                                            >
                                                This link expires in 3 days.
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td
                                    align="center"
                                    style="
                                        font-family: Montserrat, Arial, sans-serif;
                                        color: #ffffff;
                                        padding-top: 24px;
                                    "
                                >
                                Your username is <strong>{ user }</strong>
                                </td>
                            </tr>
                            <tr>
                                <td
                                    align="center"
                                    style="
                                        font-family: Montserrat, Arial, sans-serif;
                                        font-size: 18px;
                                        line-height: 22px;
                                        color: #ffffff;
                                        padding-top: 24px;
                                    "
                                >
                                    Cheers,
                                </td>
                            </tr>
                            <tr>
                                <td
                                    align="center"
                                    valign="top"
                                    style="color: #ffffff; padding-top: 24px; padding-bottom: 32px"
                                >
                                    <img
                                        src="{ signature_url }"
                                        style="
                                            width: 45%;
                                            margin-left: auto;
                                            margin-right: auto;
                                            display: block;
                                        "
                                        alt="The Keen Team"
                                    />
                                </td>
                            </tr>
                        </tbody>
                    </table>
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
                <h1>Let's Reset</h1>
                <p>This is just content no links</p>
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
