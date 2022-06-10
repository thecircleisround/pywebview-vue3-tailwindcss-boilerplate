from subprocess import Popen, PIPE
import re


def process_cmd(script):
    process = Popen(["osascript", "-e", script], stdout=PIPE)
    output = process.communicate()
    return output


def send_imessage(phone, message):
    script = f"""
    tell application "Messages"
        set targetService to 1st account whose service type = SMS
        set targetBuddy to participant "{phone}" of targetService
        send "{message}" to targetBuddy
    end tell
        """
    output = process_cmd(script)


def create_contact(lead: object, settings: object):
    script = """
    tell application "Microsoft Outlook"
        try
            set the check to get the first contact whose mobile number contains "{}"
        on error
            make new contact with properties {{first name:"{}", last name:"{}",¬
            email addresses:{{address:"{}", type:home}}, mobile number:"{}", company:"{}"}}
        end try
    end tell
    """.format(
        lead.phone, lead.first_name, lead.last_name, lead.email, lead.phone, lead.source
    )
    output = process_cmd(script)


def update_contact(lead: object, settings: object):
    script = """
    tell application "Microsoft Outlook"
        set thePerson to get the first contact whose mobile number contains "{}"
        save
    end tell
    """.format(
        lead.phone, lead.location
    )

    output = process_cmd(script)


def get_apple_message_ids():
    script = """ 
    tell application "Messages"
        get every account
    end tell
    """
    output = process_cmd(script)
    ids = re.findall("((?:\\w+-){4}\\w+)", str(output[0]))
    print("Following Apple IDs available on this system:")
    for id in ids:
        print(id)
