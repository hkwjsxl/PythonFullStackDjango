from hashlib import md5


def md5_enc(data):
    md5_obj = md5()
    md5_obj.update('冰冻三尺非一日之寒'.encode('utf-8'))
    md5_obj.update(data.encode('utf-8'))
    return md5_obj.hexdigest()
