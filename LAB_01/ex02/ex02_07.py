print(" nhap cac dong van ban (nhap 'done' dr ket thuc ):")
lines = []
while True:
    line = input()
    if line.lower() =='done':
        break
    lines.append(line)
print("\n cac dong da nhap sau khi chuyen thanh chu hoa:")
for line in lines:
    print(line.upper())
    
    
    