import sys
from formating import format_msg
from send_mail import send_mail

def send(name, website=None, to_emails=None, verbose=False):
    assert to_emails != None
    if website != None:
        msg = format_msg(name=name, website=website)
    else:
        msg = format_msg(name=name)
    
    if verbose:
        print(name, website, to_emails)

    try:
        send_mail(text=msg, to_emails=[to_emails], html=None)
        sent = True
    except:
        sent = False
    
    return sent


if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"

    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name=name, to_emails=email, verbose=True)
    print(response)


