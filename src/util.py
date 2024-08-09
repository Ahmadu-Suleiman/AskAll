def register_name(text: str):
    if text.startswith('REGISTER:'):
        return text.replace('REGISTER:', '').strip()
    else:
        return ''
