import lzma

def compress_data(data, compression_level):
    return lzma.compress(data, preset=compression_level)

def decompress_data(compressed_data):
    return lzma.decompress(compressed_data)

def file_to_binary(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def binary_to_file(data, file_path):
    with open(file_path, 'wb') as file:
        file.write(data)
