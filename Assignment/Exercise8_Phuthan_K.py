username = input("Username : ")
password = int(input("Password : "))
sweaterPrice = 800 #ราคาเสื้อกันหนาว/ตัว#
jacketPrice = 500 #ราคาเสื้อแจ็คเก็ต/ตัว#
jeansPrice = 1000 #ราคากางเกงยีนส์/ตัว#
sneakerPrice = 700 #ราคารองเท้าผ้าใบ/คู่#
suitcasePrice = 1100 #ราคาเสื้อกันหนาว/ตัว#

if username == "Phuthan"and password == 120212:
    print("------กรุณาเลือกรายการสินค้า------")
    print("1.เสื้อกันหนาว           : 800 บาท")
    print("2.เสื้อแจ็คเก็ต           : 500 บาท")
    print("3.กางเกงยีนส์           : 1000 บาท")
    print("4.รองเท้าผ้าใบ          : 700 บาท")
    print("5.กระเป๋าเดินทาง        : 1100 บาท")
    productInput = int(input("เลือกหมายเลขสินค้าที่ต้องการ ==>"))
    quantityInput = int(input("เลือกจำนวนสินค้าที่ต้องการ ==>"))
    if productInput== 1 :
        print("ราคาสินค้าทั้งหมด = ",(sweaterPrice*quantityInput),"บาท")
    elif (productInput== 2):
        print("ราคาสินค้าทั้งหมด = ",(jacketPrice*quantityInput),"บาท")
    elif (productInput== 3):
        print("ราคาสินค้าทั้งหมด = ",(jeansPrice*quantityInput),"บาท")
    elif (productInput== 4):
        print("ราคาสินค้าทั้งหมด = ",(sneakerPrice*quantityInput),"บาท")
    elif (productInput== 5):
        print("ราคาสินค้าทั้งหมด = ",(suitcasePrice*quantityInput),"บาท")
    else:
        print("คุณทำรายการไม่ถูกต้อง")
else:
    print("คุณทำรายการไม่ถูกต้อง")