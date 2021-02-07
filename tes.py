# coding:utf8
# Create By Kang Pacman Gans:v
# Tools Name : Auto Decrypt Script Python2
try:
	import os,sys, platform, uncompyle6
except ImportError:
	os.system("pip2 install uncompyle6");os.system("python2 {}".format(sys.argv[0]))
merah, hijau, cyan, putih, ungu="\x1b[1;31m", "\x1b[1;32m","\x1b[1;36m","\x1b[1;37m","\x1b[1;35m"
def echo(kon):
	print(kon)
def keluar(mati):
	exit(mati)
class KangPacmanGanteng:
	def __init__(self, file):
		self.buka=open(file,"r").read()
		self.file=self.buka.replace("exec","KangPacman=")
		self.potong=sys.argv[1].replace(".py","_dec.py")
	def AapTamvan(self):
			if "marshal.loads" in self.buka:
				try:
					if "exec" not in self.buka:keluar("{}[{}!{}]{} File {} Exec Not Detected".format(merah,hijau,merah,putih,sys.argv[1]))
					else:
						open(".cache","w").write("merah, hijau, putih='\\x1b[1;31m', '\\x1b[1;32m','\\x1b[1;37m'\nfrom uncompyle6.main import decompile as dec\nfrom sys import stdout as aapgans\n"+self.file+"\ntry:\n    dec(2.7,KangPacman,aapgans)\nexcept Exception as xnxx:\n    exit('{}[{}!{}]{} Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))") ; os.system("python2 .cache > "+self.potong) ; df=open(self.potong).read() ; open(self.potong,"w").write("# coding:utf-8\n# Decompile By Kang Pacman\n"+df+"\n# Awokawokawok Ngerekod:v")
						if "import" in df or "from" in df or "print" in df or "time.sleep" in df or "hex" in df or "print" in df or "os" in df or "sys" in df or "=" in df or "'" in df or '"' in df or "(" in df or ")" in df:os.remove(".cache") ; keluar("{}[{}✓{}]{} File Saved As : {}".format(hijau,cyan,hijau,putih,self.potong))
						else:os.remove(".cache");keluar("{}[{}!{}]{} Decompile Gagal".format(merah,hijau,merah,putih))
				except Exception as exx:keluar(str(exx))
			elif "marshal.loads" not in self.buka:
				try:
					if "exec" not in self.buka:keluar("{}[{}!{}]{} File {} Exec Not Detected".format(merah,hijau,merah,putih,sys.argv[1]))
					else:
						open(".cache","w").write(self.file+"\nmerah, hijau, putih='\x1b[1;31m', '\x1b[1;32m','\x1b[1;37m'\n\ntry:\n    print(KangPacman)\nexcept Exception as xnxx:\n    exit('{}[{}!{}]{} Error : {}'.format(merah,hijau,merah,putih,str(xnxx)))") ; os.system("python2 .cache > "+self.potong) ; df=open(self.potong).read() ; open(self.potong,"w").write("# coding:utf-8\n# Decompile By Kang Pacman\n"+df+"\n# Awokawokawok Ngerekod:v")
						if "import" in df or "from" in df or "print" in df or "time.sleep" in df or "hex" in df or "print" in df or "os" in df or "sys" in df or "=" in df or "'" in df or '"' in df or "(" in df or ")" in df:os.remove(".cache") ; keluar("{}[{}✓{}]{} File Saved As : {}".format(hijau,cyan,hijau,putih,self.potong))
						else:os.remove(".cache");keluar("{}[{}!{}]{} Decompile Gagal".format(merah,hijau,merah,putih))
				except Exception as exx:keluar(str(exx))
if __name__=="__main__":
	ver="2.7"
	if platform.python_version().split(".")[0] != "2":
		keluar("\x1b[1;31m[\x1b[1;32m!\x1b[1;31m] \x1b[1;37mHarap Gunakan Python Versi %s "%ver.split(" ")[0])
	try:
		kansnsnsnsnnsbebensmamamalalalaknwbwbwksnwvrvyctvrjsknsjdudjsjsjebebbebenenen_hdjdndndnjsnsnsn_jsjsnsnsmmemememsnsjdjdjsbsbsjaoaoqowisuusjw=KangPacmanGanteng(sys.argv[1])
		kansnsnsnsnnsbebensmamamalalalaknwbwbwksnwvrvyctvrjsknsjdudjsjsjebebbebenenen_hdjdndndnjsnsnsn_jsjsnsnsmmemememsnsjdjdjsbsbsjaoaoqowisuusjw.AapTamvan()
	except IndexError:
		keluar("{}[{}!{}] {}Usage : python2 {} file.py".format(merah,hijau,merah,putih,sys.argv[0]))
	except IOError:
		keluar("{}[{}!{}] {}File {} Not Found".format(merah,hijau,merah,putih,sys.argv[1]))
