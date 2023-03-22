from scipy.io import wavfile
import subprocess # 执行命令行
h,music = wavfile.read('./邓紫棋 - 喜欢你.wav')
part = music[60*44100:81*44100]
wavfile.write('./xihuani.wav',44100,part)
cmd = 'ffmpeg -i gray.mp4 -i xihuani.wav gray_music.mp4'
result = subprocess.call(cmd,shell=True)
print(result)