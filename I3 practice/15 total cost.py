video_type=input("enter type of video('new video or old movies'):  ")
a=video_type.lower()
days=int(input("enter number of days:  "))
if video_type=="new video":
    print("total cost is:  ",75*days)
else:
    print("total cost is:  ",50*days)
