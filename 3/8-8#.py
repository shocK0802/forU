#在为完成练习 8-7 编写的程序中，*编写一个 while 循环，让用户*输入一个专辑的歌手和名称。
# *获取这些信息后，使用它们来调用函数 make_album()，并将创建的*字典打印出来。
# 在这个 while 循环中，务必要提供退出途径。
def make_album(singer_name,album_name,songs_number=''):
    if songs_number:
        album = {'singer_name':singer_name,'album_name':album_name,'songs_number':songs_number}
    else:
        album = {'singer_name':singer_name,'album_name':album_name}
    return album



singer_name = "请输入歌手名,输入quit即退出:"
album_name = "请输入专辑名,输入quit即退出:"



action = True
while action:
	a = input(singer_name)
	b = input(album_name)
	if a == quit or b == quit:
		break
	else:
		c = make_album(a,b)
		print(c)