# coding:utf8
# Create By Kang Pacman Gans:v
# Thanks To : Rizky ID, Khairul Syabana, Nanta XE, Dan Seluruh Member Grup User Termux Newbie
try:
	import os,sys, platform, uncompyle6
except ImportError:
	os.system("pip2 install uncompyle6");os.system("python2 {}".format(sys.argv[0]))
merah, hijau, cyan, putih, ungu = "\x1b[1;31m", "\x1b[1;32m","\x1b[1;36m","\x1b[1;37m","\x1b[1;35m"

def keluar(mati):
	exit(mati)

class KonTol:
	def __init__(self, file):
		self.buka = open(file,"r").read()
		self.file = self.buka.replace("exec","Ngontol = ")
		self.potong = sys.argv[1].replace(".py","_dec.py")

	def MeKi(self):
		if "marshal.loads" in self.buka:
			if "exec" not in self.buka:
				keluar("{}[{}!{}]{} File {} Exec Not Detected".format(merah,hijau,merah,putih,sys.argv[1]))
			else:
				open(".cache","w").write("merah, hijau, putih = '\\x1b[1;31m', '\\x1b[1;32m','\\x1b[1;37m'\nfrom uncompyle6.main import decompile as dec\nfrom sys import stdout as aapgans\n"+self.file+"\ntry:\n    dec(2.7,Ngontol,aapgans)\nexcept KeyError as xnxx:\n    exit('{}[{}!{}]{} Key Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))\nexcept TypeError as xnxx:\n    exit('{}[{}!{}]{} Type Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))\nexcept Exception as xnxx:\n    exit('{}[{}!{}]{} Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))")
				os.system("python2 .cache > "+self.potong)
				df = open(self.potong).read()
				open(self.potong,"w").write("##### Decompile By Kang Pacman #####\n"+df+"\n# Awokawokawok Ngerekod:v")
				if "import" or "from" or "print" or "time.sleep" or "hex" or "print" or "os" or "sys" or "=" or "'" or '"' or "(" or ")" in self.potong:
					os.remove(".cache")
					keluar("{}[{}✓{}]{} File Saved As : {}".format(hijau,cyan,hijau,putih,self.potong))
				else:
					os.remove(".cache")
					keluar("{}[{}!{}]{} Decompile Gagal".format(merah,hijau,merah,putih))
		elif "marshal.loads" not in self.buka:
			if "exec" not in self.buka:
				keluar("{}[{}!{}]{} File {} Exec Not Detected".format(merah,hijau,merah,putih,sys.argv[1]))
			else:
				open(".cache","w").write(self.file+"\nmerah, hijau, putih = '\\x1b[1;31m', '\\x1b[1;32m','\\x1b[1;37m'\n\ntry:\n    print(Ngontol)\nexcept KeyError as xnxx:\n    exit('{}[{}!{}]{} Key Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))\nexcept TypeError as xnxx:\n    exit('{}[{}!{}]{} Type Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))\nexcept Exception as xnxx:\n    exit('{}[{}!{}]{} Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))")
				os.system("python2 .cache > "+self.potong)
				df = open(self.potong).read()
				open(self.potong,"w").write("##### Decompile By Kang Pacman #####\n"+df+"\n# Awokawokawok Ngerekod:v")
				if "import" or "from" or "print" or "time.sleep" or "hex" or "print" or "os" or "sys" or "=" or "'" or '"' or "(" or ")" in self.potong:
					os.remove(".cache")
					keluar("{}[{}✓{}]{} File Saved As : {}".format(hijau,cyan,hijau,putih,self.potong))
				else:
					os.remove(".cache")
					keluar("{}[{}!{}]{} Decompile Gagal".format(merah,hijau,merah,putih))

if __name__=="__main__":
	ver = "2.7"
	if platform.python_version().split(".")[0] != "2":
		keluar("\x1b[1;31m[\x1b[1;32m!\x1b[1;31m] \x1b[1;37mHarap Gunakan Python Versi %s "%ver.split(" ")[0])
	try:
		KonTol(sys.argv[1]).MeKi()
	except IndexError:
		keluar("{}[{}!{}] {}Usage : python2 {} file.py".format(merah,hijau,merah,putih,sys.argv[0]))
	except IOError:
		keluar("{}[{}!{}] {}File {} Not Found".format(merah,hijau,merah,putih,sys.argv[1]))
