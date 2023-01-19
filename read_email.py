import email
import imaplib
from send_email import Envs
from dotenv import load_dotenv
load_dotenv(".env")

async def read_email_message():

    imap_server = Envs.MAIL_SERVER_READ

    email_address = Envs.MAIL_USERNAME

    password = Envs.MAIL_PASSWORD

    imap = imaplib.IMAP4_SSL(imap_server)

    imap.login(email_address, password)

    imap.select("Inbox")

    _, msgnums = imap.search(None, "ALL")
    mnums = msgnums[0][::-1]
    for i in mnums.split():
        _, data = imap.fetch(i,"(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        if(msg.is_multipart()):
            for payload in msg.get_payload():
                if(payload.get_content_type() == "text/plain"):
                    return payload.get_payload(), msg.get('From')
        else:
            return msg.get_payload(), msg.get('From')
    imap.close()
