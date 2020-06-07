
def load_script():
    """
        test script
    """
    f = open('payload/mini-reverse.ps1', 'r')
    payload = f.read()
    minimize(payload)

def minimize(payload):
    """
        Minimize a script by delete unimportant character
    """
    min_payload = payload
    delete_list = ["\r", "\n", "\t"]
    for item in delete_list:
        min_payload = min_payload.replace(item, "")
    print(min_payload)

load_script()