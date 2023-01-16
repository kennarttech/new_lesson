import pyotp
import time
import qrcode




key = "lkjalkulakjlkdhlhsfye"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="kennartfoundation", 
                                            issuer_name="Kennart Tech App")



print(uri)
qrcode.make(uri).save("totp.png")