def txt_to_ascii(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            data =  file.read()
        return [ord(char) for char in data]
    except IOError as e:
        print(f'Error: {e}')
        return []
    except Exception as e:
        print(f'Error: {e}')
        return []
