import glob
from pathlib import Path

fp1 = ('D:\\All\\folder\\New folder')
list1 = [Path(f).stem for f in glob.glob(fp1 + "\*.csv")]
# list1


fp2 = ('D:\\All\\somefolder')
list2 = [Path(f).stem for f in glob.glob(fp2 + "\*.csv")]
# list2


res = [x for x in list1 + list2 if x not in list1 or x not in list2]
res
