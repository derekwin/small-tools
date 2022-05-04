# 带时间戳的txt字幕文件 转 srt格式字幕文件
# txt文件内容如下：（腾讯云语音识别导出）
# file: UIUC.mp3
# ***********************************result**************************************
# [0:15.400,1:0.480]  Brighton is a professor at UI you see, he's a technical director at vm there mhm he's perhaps well known for his very successful startup called veri flo, he was a CEO of veri flo for many years until it got acquired by VMware his research interests are sort of the systems and algorithms with a little bit of touch of verification recently got many awards and papers and maybe one of his most well-known works is to change the way that we think about networks with rate control algorithms in the Internet and so we're very excited to have you brighten and to hear your thoughts on this rate control algorithms, thank you so much for being here.
# [1:1.280,1:32.760]  Thanks so much for the invitation to speak so we'll be talking about some adventures in learning based rate control and this is a project that's been coed with UC and my collaborators at Hebrew university and particularly Michael Shapiro's group so a big thanks to him and all of the students at both a universities that really did the real work in all of this including many of the slides.
# [1:32.980,1:53.780]  Okay, so this is a this has been a long running project that I'm really began when we looked at one of the core protocols on the Internet congestion control particularly tcp congestion control foundational to you know almost all communication on the Internet.
# [1:54.060,1:55.480]  I'm.
# 
# 转换后 srt文件格式
# 0
# 00:00:15,400 --> 00:01:00,480
# Brighton is a professor at UI you see, he's a technical director at vm there mhm he's perhaps well known for his very successful startup called veri flo, he was a CEO of veri flo for many years until it got acquired by VMware his research interests are sort of the systems and algorithms with a little bit of touch of verification recently got many awards and papers and maybe one of his most well-known works is to change the way that we think about networks with rate control algorithms in the Internet and so we're very excited to have you brighten and to hear your thoughts on this rate control algorithms, thank you so much for being here.
#
# 1
# 00:01:01,280 --> 00:01:32,760
# Thanks so much for the invitation to speak so we'll be talking about some adventures in learning based rate control and this is a project that's been coed with UC and my collaborators at Hebrew university and particularly Michael Shapiro's group so a big thanks to him and all of the students at both a universities that really did the real work in all of this including many of the slides.
#
# 2
# 00:01:32,980 --> 00:01:53,780
# Okay, so this is a this has been a long running project that I'm really began when we looked at one of the core protocols on the Internet congestion control particularly tcp congestion control foundational to you know almost all communication on the Internet.
#
# 3
# 00:01:54,060 --> 00:01:55,480
# I'm.
# 

import re
from turtle import right, st
txtname = './uiuc.txt'
srtname = './uiuc.srt'

def transtime(timestr):
    strlist = timestr.replace('.',',').split(":")
    if len(strlist) < 3:
        strlist.insert(0, '00')
    if len(strlist[-1])<6:
        strlist[-1] = '0'+strlist[-1]
    if len(strlist[1])<2:
        strlist[1] = '0'+strlist[1]
    return ':'.join(strlist)

with open(srtname, 'w') as out:
    with open(txtname, 'r') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if line.startswith('['):
                out.write(str(i)+'\n')
                timelist = re.match(r'\[(.*?)\]', line).group()
                start,end = timelist[1:-1].split(",")
                # print(start, end)
                # print(transtime(start))
                out.write(transtime(start)+' --> '+transtime(end)+'\n')
                subtitle = line.split("] ")[1]
                # print(subtitle[1:])
                out.write(subtitle + '\n')
                i += 1
