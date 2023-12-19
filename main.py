# รับข้อมูลอาชีพเริ่มต้นของผู้เล่น prompt คือ "Choose a career. Start: (knight, magician, arrow): "
career = input()


# กำหนดค่าพลังพื้นฐานของแต่ละอาชีพ
knight_attack = 100
knight_defend = 150
knight_magic = 50

magician_attack = 50
magician_defend = 50
magician_magic = 150

arrow_attack = 75
arrow_defend  = 75

# ตัวแปรสำหรับใช้เก็บค่าพลังรวม
total_power = 0

# คำนวณค่าพลังรวมโดยใช้ if / else 

# ถ้า career == knight 
# ค่าพลังรวม = ค่าพลังโจมตีอัศวิน + ค่าพลังป้องกันอัศวิน

# ถ้า career == arrow 
# ค่าพลังรวม = ค่าพลังโจมตีนักธนู + ค่าพลังป้องกันนักธนู

# ถ้า career == magician
# ค่าพลังรวม = ค่าพลังโจมตีนักเวทย์ + ค่าพลังเวทย์นักเวทย์


print("The maximum power of professional players", career , "is", total_power)