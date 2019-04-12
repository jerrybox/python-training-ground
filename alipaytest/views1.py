import rsa

app_alipay_sanbox_private_path0 = r'C:\Users\jerry\Desktop\app_private_key.pem'
app_alipay_sanbox_private_path1 = r'C:\Users\jerry\Desktop\rsa_private_key.pem'

with open(app_alipay_sanbox_private_path0, 'r', encoding='utf-8') as fp:
    key_text = fp.read()

# print(key_text)

print(key_text.find('-----BEGIN RSA PRIVATE KEY-----'))


# with open(app_alipay_sanbox_private_path1, 'wb') as ofp:
#     ofp.write(key_text.encode())

rsa.PrivateKey.load_pkcs1(app_alipay_sanbox_private_path1, format='PEM')

