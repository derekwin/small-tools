from moviepy.editor import *
from pathlib import Path

def get_srcfilename(src_path='Src'):
    if (p:=Path(src_path)).exists():
        return [name for name in p.iterdir() if str(name).endswith('.mp4')]
    p.mkdir()
    print('Src目录不存在，已经创建')
    return []
# 返回的是对象列表

def create_video(srcfilename,output_name):
    if Path('Output').exists() is False:
        Path('Output').mkdir()
    clip_list=[VideoFileClip(str(clip)).rotate(90) for clip in srcfilename]
    finalvideo = concatenate_videoclips(clip_list)
    finalvideo.write_videofile(str(Path('Output')/output_name)) # fps=24


def get_output_name():
    this_path_filename_list=[str(x) for x in Path('.').iterdir() if x.is_file()]
    print("(ctrl-z退出程序)输入要保存的文件名字(不加文件后缀):")
    while (output_name:=input()+'.mp4') in this_path_filename_list:
        print('输出文件已经存在，更换名字再保存')
        print('输入新名字:')
    return output_name


if __name__ =="__main__":
    
    if (srcfilename:=get_srcfilename())==[]:
        print('Src目录下没有mp4文件')
        print('放好视频源文件，退出后重新运行')
    else:
        output_name=get_output_name()
        create_video(srcfilename,output_name)