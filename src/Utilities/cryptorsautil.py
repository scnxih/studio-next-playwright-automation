# import base64
# from Crypto.Hash import SHA256
# from Crypto.PublicKey import RSA
# from Crypto.Signature import PKCS1_v1_5
# from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
#
#
#
# class CryptoRsaUtil:
#     def __init__(self, rsa_publicKey: str = None, rsa_privateKey: str = None):
#         """
#         公钥私钥为不带开头的文本
#         这里公钥与私钥是对方给的,不是同一对秘钥(也可以是同一对)
#         :param rsa_publicKey: rsa_publicKey
#         :param rsa_privateKey: rsa_privateKey
#         """
#         self.public_key = RSA.importKey(rsa_publicKey)
#         self.private_key = RSA.importKey(rsa_privateKey)
#
#     def decrypt(self, data: str) -> str:
#         """
#         “解密”函数接收字符串“data”，使用公钥对其进行解密，并将解密后的数据作为字符串返回。
#
#         :param data: “data”参数是一个字符串，表示要解密的数据。
#         :type data: str
#         :return: “解密”函数返回一个解密的字符串。
#         """
#         data = base64.b64decode(data)
#         length = len(data)
#         print(length)
#         # default_length = 128
#         default_length = 256  # 1024bit的证书用128,2048bit证书用256位
#         # 私钥解密
#         priobj = Cipher_pkcs1_v1_5.new(self.private_key)
#         # 长度不用分段
#         if length < default_length:
#             return b''.join(priobj.decrypt(data, b' '))
#         # 需要分段
#         offset = 0
#         res = []
#         while length - offset > 0:
#             if length - offset > default_length:
#                 res.append(priobj.decrypt(data[offset:offset + default_length], b' '))
#             else:
#                 res.append(priobj.decrypt(data[offset:], b' '))
#             offset += default_length
#         res_data = b''.join(res)
#         return str(res_data, encoding='utf8')
#
#     def encrypt(self, data: str) -> str:
#         """
#         “加密”函数接收字符串“data”，使用私钥对其进行解密，并将解密后的数据作为字符串返回。
#
#         :param data: “data”参数是一个字符串，表示要加密的数据。
#         :type data: str
#         :return: “加密”函数返回一个解密的字符串。
#         """
#         length = len(data)
#         # 单次加密串的长度最大为 (key_size/8)-11,1024bit的证书用100, 2048bit的证书用 200
#         default_length = 117
#         # default_length = 100
#         # 公钥加密
#         pubobj = Cipher_pkcs1_v1_5.new(self.public_key)
#         # 长度不用分段
#         if length < default_length:
#             return str(base64.b64encode(pubobj.encrypt(data.encode('utf-8'))), encoding='utf8')
#         # 需要分段
#         offset = 0
#         res = []
#         while length - offset > 0:
#             if length - offset > default_length:
#                 res.append(pubobj.encrypt(data[offset:offset + default_length].encode('utf-8')))
#             else:
#                 res.append(pubobj.encrypt(data[offset:].encode('utf-8')))
#             offset += default_length
#         byte_data = b''.join(res)
#
#         return str(base64.b64encode(byte_data), encoding='utf8')
#
#     def sign(self, data: str) -> str:
#         """
#         “签名”函数接收字符串“data”，使用私钥对其进行签名，并将签名后的数据作为字符串返回。
#
#         :param data: “data”参数是一个字符串，表示要签名的数据。
#         :type data: str
#         :return: “签名”函数返回一个签名的字符串。
#         """
#         data = data.encode('utf-8')
#         hash_obj = SHA256.new(data)
#         signer = PKCS1_v1_5.new(self.private_key)
#         signature = signer.sign(hash_obj)
#         return str(base64.b64encode(signature), encoding='utf8')
#
#     def verify(self, data: str, sign: str) -> bool:
#         if isinstance(data, str):
#             data = data.encode('utf-8')
#         if isinstance(sign, str):
#             sign = sign.encode('utf-8')
#         # data做“哈希”处理,RSA签名这么要求的
#         hash_obj = SHA256.new(data)
#         try:
#             # 因为签名被base64编码,所以这里先解码,再验签
#             PKCS1_v1_5.new(self.public_key).verify(hash_obj, base64.b64decode(sign))
#             print('The signature is valid.')
#             return True
#         except (ValueError, TypeError):
#             print('The signature is invalid.')
#             return False
#
