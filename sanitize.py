import re

def sanitize_string_template():
    string_template = input("Paste: ")
    if not re.search(r'(?s)(?=.*\$)(?=.*\{)(?=.*\})(?=.*,)', string_template):
        print("Please provide a valid string template format.")
        sanitize_string_template()
    else:
        new_string_template = re.sub(r"\$", "", string_template)
        print("")
        print(new_string_template)
        return

sanitize_string_template()