# This is a sample Python script.
import ffmpeg


directory = '/Users/hokageminato/Downloads/Video_Recording_0__26-07-2024/'

print('Conversion Started')

(
    ffmpeg
    .input(f'{directory}SS_%d.jpg')
    .filter('scale', 'if(mod(iw,2),iw+1,iw)', 'if(mod(ih,2),ih+1,ih)')
    .output(f'{directory}/movie.mp4')
    .overwrite_output()
    .run()
)


print('Conversion Successful')