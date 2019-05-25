import struct


def tamper(student_id):
  with open('lenna.bmp','r+b')as f:#以二进制方式打开文件
   f.seek(54)#找到最后一行
   f.read(3)#从当前位置起，读取三个字节
  for i in student_id:
        if i==0:
              i=10
              i+=1#跳过i个格子改下一个格子的像素点吗
              f.read(i*3)
              black=b'\x00\x00\x00'
              f.write(black)
  f.close()


        
        


def detect():
  with open('lenna.bmp', 'rb') as f:
    bmp_file_header = f.read(14)

    bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

    f.seek(offset)

    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)

      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset
        count -= 1

      offset += 1


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()
