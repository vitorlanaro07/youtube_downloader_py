from pydub import AudioSegment
from ffmpeg import *
import os


audio = AudioSegment.from_file("/home/vitorlanaro/Downloads/resp_cecy_230622.aac", format="aac")

audio.export("/home/vitorlanaro/resp_cecy_230622.mp3", format="mp3")

