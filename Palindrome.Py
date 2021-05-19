def pal():
	return s == s[::-1]
s = "heheheh"
if pal():
	print("yes")
else:
	print('no')
pal()