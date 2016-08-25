import webbrowser
import time

print("Started: " + time.ctime());

breaks_limit = 3
breaks_count = 0

while(breaks_count < breaks_limit):
    time.sleep(2*60*60)
	print(time.ctime())
	print("Come on... It's time for a break. Here's your favorite song...")
    webbrowser.open("https://www.youtube.com/watch?v=chmCtZTSUWI")
    breaks_count += 1

print("Ended: " + time.ctime());
