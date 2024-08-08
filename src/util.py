t = 'REGISTER: Umar Farouk'


def register_name(text: str):
    if text.upper().startswith('REGISTER:'):
        return text.replace('REGISTER:', '').strip()
    else:
        return ''
