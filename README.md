```bash
source venv-p/bin/activate
```

#1 
```bash
~/homework-1 > cd venv-p                                                                                                                                              venv-p
~/homework-1/venv-p > python ../super-script.py --print all --location RUN_PATH                                                                                       venv-p
pyvenv.cfg
bin
include
lib
```

#2
```bash
~/homework-1/venv-p > python ../super-script.py --print all --location SCRIPT_PATH                                                                                                 venv-p
output.json
super-script.py
output.csv
README.md
.gitignore
output.html
homework-1.iml
output.txt
venv-p
.git
.idea
```

#3
```bash
~/homework-1/venv-p > python ../super-script.py --print all --location DEFINED_PATH -p ../.idea                                                                       venv-p
vcs.xml
.gitignore
workspace.xml
modules.xml
misc.xml
```

#4
```bash
~/homework-1/venv-p > python ../super-script.py --print all --location RUN_PATH -r ../.idea                                                                          venv-p
vcs.xml
.gitignore
workspace.xml
modules.xml
misc.xml
~/homework-1/venv-p > python ../super-script.py --print all --location RUN_PATH -r ../venv-p                                                                         venv-p
pyvenv.cfg
bin
include
lib
~/homework-1/venv-p > python ../super-script.py --print all --location SCRIPT_PATH -s ../venv-p                                                                      venv-p
pyvenv.cfg
bin
include
lib
```

#5
```bash
~/homework-1/venv-p > python ../super-script.py --print directories --location SCRIPT_PATH                                                                            venv-p
venv-p
.git
.idea
~/homework-1/venv-p > python ../super-script.py --print files --location SCRIPT_PATH                                                                                  venv-p
output.json
super-script.py
output.csv
README.md
.gitignore
output.html
homework-1.iml
output.txt
```

#6
```bash
~/homework-1/venv-p > python ../super-script.py --print all -v                                                                                                        venv-p
Files in RUN_PATH ~/homework-1/venv-p
   size                              hash    owner        m_date        c_date       type        name                                               path                                          full_path
0   104  bcef45293437a3322242da598cadf572  user  1.656075e+09  1.656075e+09       file  pyvenv.cfg  /Users/user/Documents/homework-1/...  /Users/user/Documents/homework-1/...
1   544  a2862972276cb45bde8587a7142be116  user  1.656244e+09  1.656244e+09  directory         bin  /Users/user/Documents/homework-1/...  /Users/user/Documents/homework-1/...
2    64  d41d8cd98f00b204e9800998ecf8427e  user  1.656075e+09  1.656075e+09  directory     include  /Users/user/Documents/homework-1/...  /Users/user/Documents/homework-1/...
3    96  b417db27b39f893355bee6832fe176d6  user  1.656075e+09  1.656075e+09  directory         lib  /Users/user/Documents/homework-1/...  /Users/user/Documents/homework-1/...
~/homework-1/venv-p > python ../super-script.py --print all -l                                                                                                        venv-p
pyvenv.cfg
bin
include
lib
```

#7 
```bash
~/homework-1/venv-p > python ../super-script.py --print all --utc -v                                                                                                  venv-p
Files in RUN_PATH ~/homework-1/venv-p
   size                              hash    owner                      m_date                      c_date       type        name                                               path                                          full_path
0   104  bcef45293437a3322242da598cadf572  user  2022-06-24 12:48:22.717272  2022-06-24 12:48:22.717272       file  pyvenv.cfg  /Users/user/Documents/homework-1/...  /Users/user/Documents/homework-1/...
1   544  a2862972276cb45bde8587a7142be116  user  2022-06-26 11:47:30.941399  2022-06-26 11:47:30.941399  directory         bin  /Users/user/Documents/homework-1/...  /Users/user/Documents/homework-1/...
2    64  d41d8cd98f00b204e9800998ecf8427e  user  2022-06-24 12:48:22.716662  2022-06-24 12:48:22.716662  directory     include  /Users/user/Documents/homework-1/...  /Users/user/Documents/homework-1/...
3    96  b417db27b39f893355bee6832fe176d6  user  2022-06-24 12:48:22.716856  2022-06-24 12:48:22.716856  directory         lib  /Users/user/Documents/homework-1/...  /Users/user/Documents/homework-1/...
```

#8
```bash
~/homework-1 > python super-script.py --print all --utc -v -c                                                                                                         venv-p
Files in RUN_PATH ~/homework-1
    size                              hash    owner                      m_date                      c_date       type             name                                           path                                          full_path
0   2711  71313849ff4ce59ae543130fb079dd3a  user  2022-06-26 11:40:31.702139  2022-06-26 11:40:31.702139       file      output.json  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
1   9335  28f7662daaf3061bddd44dc379f14689  user  2022-06-26 12:28:38.704131  2022-06-26 12:28:38.704131       file  super-script.py  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
2    967  dedc18e068839b556aab6054768b6eca  user  2022-06-26 12:36:10.016745  2022-06-26 12:36:10.016745       file       output.csv  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
3   4996  40ed71095a048923865e3af12d87c6d2  user  2022-06-26 12:36:01.919195  2022-06-26 12:36:01.919195       file        README.md  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
4     21  49823a964744934bca2fc8b09bfc940c  user  2022-06-24 12:53:55.952321  2022-06-24 12:53:55.952321       file       .gitignore  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
5   3408  79bc53cbca15e710bf6bc1a5d5a5d98f  user  2022-06-26 11:57:13.336925  2022-06-26 11:57:13.336925       file      output.html  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
6    408  264f46e4f2bfb405e512f693208bc4e9  user  2022-06-24 12:48:42.155170  2022-06-24 12:48:42.155170       file   homework-1.iml  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
7      0  d41d8cd98f00b204e9800998ecf8427e  user  2022-06-26 11:57:05.534574  2022-06-26 11:57:05.534574       file       output.txt  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
8    192  19017a9fc76e0850de1b0d5f689ecddf  user  2022-06-24 12:48:22.717120  2022-06-24 12:48:22.717120  directory           venv-p  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
9    384  7ea0218ffc9efdb10c2151aec25dbd7f  user  2022-06-26 12:03:04.753989  2022-06-26 12:03:04.753989  directory             .git  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
10   224  b2d26951b3bb45486c1a45dd5f4ce33a  user  2022-06-26 12:24:35.989021  2022-06-26 12:24:35.989021  directory            .idea  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
~/homework-1 > cat output.csv                                                                                                                                         venv-p
size,hash,owner,m_date,c_date,type,name,path,full_path
2711,71313849ff4ce59ae543130fb079dd3a,user,2022-06-26 11:40:31.702139,2022-06-26 11:40:31.702139,file,output.json,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/output.json
9335,28f7662daaf3061bddd44dc379f14689,user,2022-06-26 12:28:38.704131,2022-06-26 12:28:38.704131,file,super-script.py,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/super-script.py
967,dedc18e068839b556aab6054768b6eca,user,2022-06-26 12:36:10.016745,2022-06-26 12:36:10.016745,file,output.csv,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/output.csv
4996,40ed71095a048923865e3af12d87c6d2,user,2022-06-26 12:36:01.919195,2022-06-26 12:36:01.919195,file,README.md,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/README.md
21,49823a964744934bca2fc8b09bfc940c,user,2022-06-24 12:53:55.952321,2022-06-24 12:53:55.952321,file,.gitignore,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/.gitignore
3408,79bc53cbca15e710bf6bc1a5d5a5d98f,user,2022-06-26 11:57:13.336925,2022-06-26 11:57:13.336925,file,output.html,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/output.html
408,264f46e4f2bfb405e512f693208bc4e9,user,2022-06-24 12:48:42.155170,2022-06-24 12:48:42.155170,file,homework-1.iml,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/homework-1.iml
0,d41d8cd98f00b204e9800998ecf8427e,user,2022-06-26 11:57:05.534574,2022-06-26 11:57:05.534574,file,output.txt,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/output.txt
192,19017a9fc76e0850de1b0d5f689ecddf,user,2022-06-24 12:48:22.717120,2022-06-24 12:48:22.717120,directory,venv-p,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/venv-p
384,7ea0218ffc9efdb10c2151aec25dbd7f,user,2022-06-26 12:03:04.753989,2022-06-26 12:03:04.753989,directory,.git,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/.git
224,b2d26951b3bb45486c1a45dd5f4ce33a,user,2022-06-26 12:24:35.989021,2022-06-26 12:24:35.989021,directory,.idea,/Users/user/Documents/homework-1,/Users/user/Documents/homework-1/.idea

~/homework-1 >  python super-script.py --print all --utc -v -j                                                                                                         venv-p
Files in RUN_PATH ~/homework-1
     size                              hash    owner                      m_date                      c_date       type             name                                           path                                          full_path
0    2711  71313849ff4ce59ae543130fb079dd3a  user  2022-06-26 11:40:31.702139  2022-06-26 11:40:31.702139       file      output.json  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
1    9335  28f7662daaf3061bddd44dc379f14689  user  2022-06-26 12:28:38.704131  2022-06-26 12:28:38.704131       file  super-script.py  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
2    2471  ed5561767deb87e058a3befb4d040da9  user  2022-06-26 12:36:35.002013  2022-06-26 12:36:35.002013       file       output.csv  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
3   10645  183d5a119ea86339a88ccd5932dacebc  user  2022-06-26 12:38:23.872911  2022-06-26 12:38:23.872911       file        README.md  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
4      21  49823a964744934bca2fc8b09bfc940c  user  2022-06-24 12:53:55.952321  2022-06-24 12:53:55.952321       file       .gitignore  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
5    3408  79bc53cbca15e710bf6bc1a5d5a5d98f  user  2022-06-26 11:57:13.336925  2022-06-26 11:57:13.336925       file      output.html  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
6     408  264f46e4f2bfb405e512f693208bc4e9  user  2022-06-24 12:48:42.155170  2022-06-24 12:48:42.155170       file   homework-1.iml  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
7       0  d41d8cd98f00b204e9800998ecf8427e  user  2022-06-26 11:57:05.534574  2022-06-26 11:57:05.534574       file       output.txt  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
8     192  19017a9fc76e0850de1b0d5f689ecddf  user  2022-06-24 12:48:22.717120  2022-06-24 12:48:22.717120  directory           venv-p  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
9     384  7ea0218ffc9efdb10c2151aec25dbd7f  user  2022-06-26 12:03:04.753989  2022-06-26 12:03:04.753989  directory             .git  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
10    224  b2d26951b3bb45486c1a45dd5f4ce33a  user  2022-06-26 12:24:35.989021  2022-06-26 12:24:35.989021  directory            .idea  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
~/homework-1 > cat output.json                                                                                                                                        venv-p
[
    {
        "c_date": "2022-06-26 11:40:31.702139",
        "full_path": "/Users/user/Documents/homework-1/output.json",
        "hash": "71313849ff4ce59ae543130fb079dd3a",
        "m_date": "2022-06-26 11:40:31.702139",
        "name": "output.json",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 2711,
        "type": "file"
    },
    {
        "c_date": "2022-06-26 12:28:38.704131",
        "full_path": "/Users/user/Documents/homework-1/super-script.py",
        "hash": "28f7662daaf3061bddd44dc379f14689",
        "m_date": "2022-06-26 12:28:38.704131",
        "name": "super-script.py",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 9335,
        "type": "file"
    },
    {
        "c_date": "2022-06-26 12:36:35.002013",
        "full_path": "/Users/user/Documents/homework-1/output.csv",
        "hash": "ed5561767deb87e058a3befb4d040da9",
        "m_date": "2022-06-26 12:36:35.002013",
        "name": "output.csv",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 2471,
        "type": "file"
    },
    {
        "c_date": "2022-06-26 12:38:23.872911",
        "full_path": "/Users/user/Documents/homework-1/README.md",
        "hash": "183d5a119ea86339a88ccd5932dacebc",
        "m_date": "2022-06-26 12:38:23.872911",
        "name": "README.md",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 10645,
        "type": "file"
    },
    {
        "c_date": "2022-06-24 12:53:55.952321",
        "full_path": "/Users/user/Documents/homework-1/.gitignore",
        "hash": "49823a964744934bca2fc8b09bfc940c",
        "m_date": "2022-06-24 12:53:55.952321",
        "name": ".gitignore",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 21,
        "type": "file"
    },
    {
        "c_date": "2022-06-26 11:57:13.336925",
        "full_path": "/Users/user/Documents/homework-1/output.html",
        "hash": "79bc53cbca15e710bf6bc1a5d5a5d98f",
        "m_date": "2022-06-26 11:57:13.336925",
        "name": "output.html",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 3408,
        "type": "file"
    },
    {
        "c_date": "2022-06-24 12:48:42.155170",
        "full_path": "/Users/user/Documents/homework-1/homework-1.iml",
        "hash": "264f46e4f2bfb405e512f693208bc4e9",
        "m_date": "2022-06-24 12:48:42.155170",
        "name": "homework-1.iml",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 408,
        "type": "file"
    },
    {
        "c_date": "2022-06-26 11:57:05.534574",
        "full_path": "/Users/user/Documents/homework-1/output.txt",
        "hash": "d41d8cd98f00b204e9800998ecf8427e",
        "m_date": "2022-06-26 11:57:05.534574",
        "name": "output.txt",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 0,
        "type": "file"
    },
    {
        "c_date": "2022-06-24 12:48:22.717120",
        "full_path": "/Users/user/Documents/homework-1/venv-p",
        "hash": "19017a9fc76e0850de1b0d5f689ecddf",
        "m_date": "2022-06-24 12:48:22.717120",
        "name": "venv-p",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 192,
        "type": "directory"
    },
    {
        "c_date": "2022-06-26 12:03:04.753989",
        "full_path": "/Users/user/Documents/homework-1/.git",
        "hash": "7ea0218ffc9efdb10c2151aec25dbd7f",
        "m_date": "2022-06-26 12:03:04.753989",
        "name": ".git",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 384,
        "type": "directory"
    },
    {
        "c_date": "2022-06-26 12:24:35.989021",
        "full_path": "/Users/user/Documents/homework-1/.idea",
        "hash": "b2d26951b3bb45486c1a45dd5f4ce33a",
        "m_date": "2022-06-26 12:24:35.989021",
        "name": ".idea",
        "owner": "user",
        "path": "/Users/user/Documents/homework-1",
        "size": 224,
        "type": "directory"
    }
]

~/homework-1 > python super-script.py --print all --utc -v -t                                                                                                         venv-p
Files in RUN_PATH ~/homework-1
     size                              hash    owner                      m_date                      c_date       type             name                                           path                                          full_path
0    4509  1994197ceaaa4cd0badb48ffac9d0fb0  user  2022-06-26 12:38:29.042098  2022-06-26 12:38:29.042098       file      output.json  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
1    9335  28f7662daaf3061bddd44dc379f14689  user  2022-06-26 12:28:38.704131  2022-06-26 12:28:38.704131       file  super-script.py  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
2    2471  ed5561767deb87e058a3befb4d040da9  user  2022-06-26 12:36:35.002013  2022-06-26 12:36:35.002013       file       output.csv  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
3   18362  81461a7fb82b42ab7581a2d38224581e  user  2022-06-26 12:40:07.770999  2022-06-26 12:40:07.770999       file        README.md  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
4      21  49823a964744934bca2fc8b09bfc940c  user  2022-06-24 12:53:55.952321  2022-06-24 12:53:55.952321       file       .gitignore  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
5    3408  79bc53cbca15e710bf6bc1a5d5a5d98f  user  2022-06-26 11:57:13.336925  2022-06-26 11:57:13.336925       file      output.html  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
6     408  264f46e4f2bfb405e512f693208bc4e9  user  2022-06-24 12:48:42.155170  2022-06-24 12:48:42.155170       file   homework-1.iml  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
7       0  d41d8cd98f00b204e9800998ecf8427e  user  2022-06-26 11:57:05.534574  2022-06-26 11:57:05.534574       file       output.txt  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
8     192  19017a9fc76e0850de1b0d5f689ecddf  user  2022-06-24 12:48:22.717120  2022-06-24 12:48:22.717120  directory           venv-p  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
9     384  7ea0218ffc9efdb10c2151aec25dbd7f  user  2022-06-26 12:03:04.753989  2022-06-26 12:03:04.753989  directory             .git  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
10    224  b2d26951b3bb45486c1a45dd5f4ce33a  user  2022-06-26 12:24:35.989021  2022-06-26 12:24:35.989021  directory            .idea  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
~/homework-1 > cat output.txt                                                                                                                                         venv-p
 size                             hash   owner                     m_date                     c_date      type            name                                          path                                                     full_path
 4509 1994197ceaaa4cd0badb48ffac9d0fb0 user 2022-06-26 12:38:29.042098 2022-06-26 12:38:29.042098      file     output.json /Users/user/Documents/homework-1     /Users/user/Documents/homework-1/output.json
 9335 28f7662daaf3061bddd44dc379f14689 user 2022-06-26 12:28:38.704131 2022-06-26 12:28:38.704131      file super-script.py /Users/user/Documents/homework-1 /Users/user/Documents/homework-1/super-script.py
 2471 ed5561767deb87e058a3befb4d040da9 user 2022-06-26 12:36:35.002013 2022-06-26 12:36:35.002013      file      output.csv /Users/user/Documents/homework-1      /Users/user/Documents/homework-1/output.csv
18362 81461a7fb82b42ab7581a2d38224581e user 2022-06-26 12:40:07.770999 2022-06-26 12:40:07.770999      file       README.md /Users/user/Documents/homework-1       /Users/user/Documents/homework-1/README.md
   21 49823a964744934bca2fc8b09bfc940c user 2022-06-24 12:53:55.952321 2022-06-24 12:53:55.952321      file      .gitignore /Users/user/Documents/homework-1      /Users/user/Documents/homework-1/.gitignore
 3408 79bc53cbca15e710bf6bc1a5d5a5d98f user 2022-06-26 11:57:13.336925 2022-06-26 11:57:13.336925      file     output.html /Users/user/Documents/homework-1     /Users/user/Documents/homework-1/output.html
  408 264f46e4f2bfb405e512f693208bc4e9 user 2022-06-24 12:48:42.155170 2022-06-24 12:48:42.155170      file  homework-1.iml /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/homework-1.iml
    0 d41d8cd98f00b204e9800998ecf8427e user 2022-06-26 11:57:05.534574 2022-06-26 11:57:05.534574      file      output.txt /Users/user/Documents/homework-1      /Users/user/Documents/homework-1/output.txt
  192 19017a9fc76e0850de1b0d5f689ecddf user 2022-06-24 12:48:22.717120 2022-06-24 12:48:22.717120 directory          venv-p /Users/user/Documents/homework-1          /Users/user/Documents/homework-1/venv-p
  384 7ea0218ffc9efdb10c2151aec25dbd7f user 2022-06-26 12:03:04.753989 2022-06-26 12:03:04.753989 directory            .git /Users/user/Documents/homework-1            /Users/user/Documents/homework-1/.git
  224 b2d26951b3bb45486c1a45dd5f4ce33a user 2022-06-26 12:24:35.989021 2022-06-26 12:24:35.989021 directory           .idea /Users/user/Documents/homework-1           /Users/user/Documents/homework-1/.idea
```

#10
```bash
~/homework-1 > python super-script.py --print all --utc -v -h                                                                                                         venv-p
Files in RUN_PATH ~/homework-1
     size                              hash    owner                      m_date                      c_date       type             name                                           path                                          full_path
0    4509  1994197ceaaa4cd0badb48ffac9d0fb0  user  2022-06-26 12:38:29.042098  2022-06-26 12:38:29.042098       file      output.json  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
1    9335  28f7662daaf3061bddd44dc379f14689  user  2022-06-26 12:28:38.704131  2022-06-26 12:28:38.704131       file  super-script.py  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
2    2471  ed5561767deb87e058a3befb4d040da9  user  2022-06-26 12:36:35.002013  2022-06-26 12:36:35.002013       file       output.csv  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
3   24401  032c9a30fa55fc07c92d0c1608aa720c  user  2022-06-26 12:41:14.618150  2022-06-26 12:41:14.618150       file        README.md  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
4      21  49823a964744934bca2fc8b09bfc940c  user  2022-06-24 12:53:55.952321  2022-06-24 12:53:55.952321       file       .gitignore  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
5    3408  79bc53cbca15e710bf6bc1a5d5a5d98f  user  2022-06-26 11:57:13.336925  2022-06-26 11:57:13.336925       file      output.html  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
6     408  264f46e4f2bfb405e512f693208bc4e9  user  2022-06-24 12:48:42.155170  2022-06-24 12:48:42.155170       file   homework-1.iml  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
7    2819  d9fed496ee3a75dd083fc228fce77712  user  2022-06-26 12:40:11.496188  2022-06-26 12:40:11.496188       file       output.txt  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
8     192  19017a9fc76e0850de1b0d5f689ecddf  user  2022-06-24 12:48:22.717120  2022-06-24 12:48:22.717120  directory           venv-p  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
9     384  7ea0218ffc9efdb10c2151aec25dbd7f  user  2022-06-26 12:03:04.753989  2022-06-26 12:03:04.753989  directory             .git  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
10    224  b2d26951b3bb45486c1a45dd5f4ce33a  user  2022-06-26 12:24:35.989021  2022-06-26 12:24:35.989021  directory            .idea  /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/...
~/homework-1 > cat output.html                                                                                                                                        venv-p
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>size</th>
      <th>hash</th>
      <th>owner</th>
      <th>m_date</th>
      <th>c_date</th>
      <th>type</th>
      <th>name</th>
      <th>path</th>
      <th>full_path</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>4509</td>
      <td>1994197ceaaa4cd0badb48ffac9d0fb0</td>
      <td>user</td>
      <td>2022-06-26 12:38:29.042098</td>
      <td>2022-06-26 12:38:29.042098</td>
      <td>file</td>
      <td>output.json</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/output.json</td>
    </tr>
    <tr>
      <td>9335</td>
      <td>28f7662daaf3061bddd44dc379f14689</td>
      <td>user</td>
      <td>2022-06-26 12:28:38.704131</td>
      <td>2022-06-26 12:28:38.704131</td>
      <td>file</td>
      <td>super-script.py</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/super-script.py</td>
    </tr>
    <tr>
      <td>2471</td>
      <td>ed5561767deb87e058a3befb4d040da9</td>
      <td>user</td>
      <td>2022-06-26 12:36:35.002013</td>
      <td>2022-06-26 12:36:35.002013</td>
      <td>file</td>
      <td>output.csv</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/output.csv</td>
    </tr>
    <tr>
      <td>24401</td>
      <td>032c9a30fa55fc07c92d0c1608aa720c</td>
      <td>user</td>
      <td>2022-06-26 12:41:14.618150</td>
      <td>2022-06-26 12:41:14.618150</td>
      <td>file</td>
      <td>README.md</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/README.md</td>
    </tr>
    <tr>
      <td>21</td>
      <td>49823a964744934bca2fc8b09bfc940c</td>
      <td>user</td>
      <td>2022-06-24 12:53:55.952321</td>
      <td>2022-06-24 12:53:55.952321</td>
      <td>file</td>
      <td>.gitignore</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/.gitignore</td>
    </tr>
    <tr>
      <td>3408</td>
      <td>79bc53cbca15e710bf6bc1a5d5a5d98f</td>
      <td>user</td>
      <td>2022-06-26 11:57:13.336925</td>
      <td>2022-06-26 11:57:13.336925</td>
      <td>file</td>
      <td>output.html</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/output.html</td>
    </tr>
    <tr>
      <td>408</td>
      <td>264f46e4f2bfb405e512f693208bc4e9</td>
      <td>user</td>
      <td>2022-06-24 12:48:42.155170</td>
      <td>2022-06-24 12:48:42.155170</td>
      <td>file</td>
      <td>homework-1.iml</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/homework-1.iml</td>
    </tr>
    <tr>
      <td>2819</td>
      <td>d9fed496ee3a75dd083fc228fce77712</td>
      <td>user</td>
      <td>2022-06-26 12:40:11.496188</td>
      <td>2022-06-26 12:40:11.496188</td>
      <td>file</td>
      <td>output.txt</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/output.txt</td>
    </tr>
    <tr>
      <td>192</td>
      <td>19017a9fc76e0850de1b0d5f689ecddf</td>
      <td>user</td>
      <td>2022-06-24 12:48:22.717120</td>
      <td>2022-06-24 12:48:22.717120</td>
      <td>directory</td>
      <td>venv-p</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/venv-p</td>
    </tr>
    <tr>
      <td>384</td>
      <td>7ea0218ffc9efdb10c2151aec25dbd7f</td>
      <td>user</td>
      <td>2022-06-26 12:03:04.753989</td>
      <td>2022-06-26 12:03:04.753989</td>
      <td>directory</td>
      <td>.git</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/.git</td>
    </tr>
    <tr>
      <td>224</td>
      <td>b2d26951b3bb45486c1a45dd5f4ce33a</td>
      <td>user</td>
      <td>2022-06-26 12:24:35.989021</td>
      <td>2022-06-26 12:24:35.989021</td>
      <td>directory</td>
      <td>.idea</td>
      <td>/Users/user/Documents/homework-1</td>
      <td>/Users/user/Documents/homework-1/.idea</td>
    </tr>
  </tbody>
</table>
```

#11
```bash
~/homework-1 >  python super-script.py --read output.txt                                                                 venv-p
 size                             hash   owner                     m_date                     c_date      type            name                                          path                                                     full_path
 4509 1994197ceaaa4cd0badb48ffac9d0fb0 user 2022-06-26 12:38:29.042098 2022-06-26 12:38:29.042098      file     output.json /Users/user/Documents/homework-1     /Users/user/Documents/homework-1/output.json
 9335 28f7662daaf3061bddd44dc379f14689 user 2022-06-26 12:28:38.704131 2022-06-26 12:28:38.704131      file super-script.py /Users/user/Documents/homework-1 /Users/user/Documents/homework-1/super-script.py
 2471 ed5561767deb87e058a3befb4d040da9 user 2022-06-26 12:36:35.002013 2022-06-26 12:36:35.002013      file      output.csv /Users/user/Documents/homework-1      /Users/user/Documents/homework-1/output.csv
18362 81461a7fb82b42ab7581a2d38224581e user 2022-06-26 12:40:07.770999 2022-06-26 12:40:07.770999      file       README.md /Users/user/Documents/homework-1       /Users/user/Documents/homework-1/README.md
   21 49823a964744934bca2fc8b09bfc940c user 2022-06-24 12:53:55.952321 2022-06-24 12:53:55.952321      file      .gitignore /Users/user/Documents/homework-1      /Users/user/Documents/homework-1/.gitignore
 3408 79bc53cbca15e710bf6bc1a5d5a5d98f user 2022-06-26 11:57:13.336925 2022-06-26 11:57:13.336925      file     output.html /Users/user/Documents/homework-1     /Users/user/Documents/homework-1/output.html
  408 264f46e4f2bfb405e512f693208bc4e9 user 2022-06-24 12:48:42.155170 2022-06-24 12:48:42.155170      file  homework-1.iml /Users/user/Documents/homework-1  /Users/user/Documents/homework-1/homework-1.iml
    0 d41d8cd98f00b204e9800998ecf8427e user 2022-06-26 11:57:05.534574 2022-06-26 11:57:05.534574      file      output.txt /Users/user/Documents/homework-1      /Users/user/Documents/homework-1/output.txt
  192 19017a9fc76e0850de1b0d5f689ecddf user 2022-06-24 12:48:22.717120 2022-06-24 12:48:22.717120 directory          venv-p /Users/user/Documents/homework-1          /Users/user/Documents/homework-1/venv-p
  384 7ea0218ffc9efdb10c2151aec25dbd7f user 2022-06-26 12:03:04.753989 2022-06-26 12:03:04.753989 directory            .git /Users/user/Documents/homework-1            /Users/user/Documents/homework-1/.git
  224 b2d26951b3bb45486c1a45dd5f4ce33a user 2022-06-26 12:24:35.989021 2022-06-26 12:24:35.989021 directory           .idea /Users/user/Documents/homework-1           /Users/user/Documents/homework-1/.idea
```