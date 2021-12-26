from download_thread import DownloadThread
from decript_thread import DecriptThread
from combiner import Combiner
import queue

url1 = 'https://advancedpython.000webhostapp.com/s1.txt'
url2 = 'https://advancedpython.000webhostapp.com/s2.txt'
url3 = 'https://advancedpython.000webhostapp.com/s3.txt'

download_thread_1 = DownloadThread(url1, 's1_enc.txt')
download_thread_2 = DownloadThread(url2, 's2_enc.txt')
download_thread_3 = DownloadThread(url3, 's3_enc.txt')

download_thread_1.start()
download_thread_2.start()
download_thread_3.start()

download_thread_1.join()
download_thread_2.join()
download_thread_3.join()

que = queue.Queue()

t1 = DecriptThread(que, 1, 's1_enc.txt')
t2 = DecriptThread(que, 2, 's2_enc.txt')
t3 = DecriptThread(que, 3, 's3_enc.txt')

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

combiner = Combiner(que)

combiner.write_to_file('s_final.txt')
combiner.print()

