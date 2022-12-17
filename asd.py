import qrcode
email= input("enter the email")
password=input("enter the password")
imagename=input("enter image name for qr code")
data=("email = "+email+" "+"\n password = "+password)
code=qrcode.make(data)
code.save(imagename+".png")
