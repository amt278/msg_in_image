#                                          PNG
end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

with open('image.png', 'ab') as f:
    f.write(b'a7a di eshtghlt')

with open('image.png', 'rb') as f:
    content = f.read()
    offset = content.index(end_hex)
    f.seek(offset + len(end_hex))
    print(f.read())


#                                          JPG
with open('pp.jpg', 'ab') as f:
    f.write(b'a7a di eshtghlt')

with open('pp.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))
    f.seek(offset + 2)
    print(f.read())