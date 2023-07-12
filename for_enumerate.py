# for entry in enumerate(['A', 'B', 'C']):
#      print(entry)

for i, data in enumerate(['A', 'B', 'C']):
     print(f'{i}번째는 {data}입니다.')
     print('%d 번째는 %s 입니다.' %(i,data))
     print('{} 번째는 {} 입니다.' .format(i,data))
    #  print(data)
     print('------')

# for _ , data in enumerate(['A', 'B', 'C']):
#      print(data)
#      print('------')