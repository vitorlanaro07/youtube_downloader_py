from pydub import AudioSegment
from ffmpeg import *
import os

audio = AudioSegment.from_file("/home/vitorlanaro/Downloads/áudio_para_cecy_20_06_22.aac", format="aac")

audio.export("/home/vitorlanaro/áudio_para_cecy_20_06_22.m4a", format="m4a")

print("Carregando")

