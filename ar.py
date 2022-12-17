import qrcode
dt= "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
code=qrcode.make(dt)
code.save("rolled.png")