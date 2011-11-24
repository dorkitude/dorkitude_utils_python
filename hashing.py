import md5
import base64
import zlib

def to_md5(hashable):
    # create a hashed key
    m = md5.new()
    m.update(hashable)
    return m.hexdigest()

def to_compressed(string):
    return base64.b64encode(zlib.compress(string))
