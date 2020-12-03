msg_template = """Hello {name}
Thank you for joining {website}. We are very 
happy to have you with us.
"""

def format_msg(name='Saurabh', website='www.example.com'):
    formated_msg = msg_template.format(name=name, website=website)
    return formated_msg

if __name__ == "__main__":
    print(format_msg())