# Get instance
import instaloader

L = instaloader.Instaloader()

# Login or load session
username = "xxxxxxxxxxxx"
password = "xxxxxxxxxxxx"
L.login(username, password)  # (login)
txt = input('the usrs list (seprate with , ):')
targelist = txt.split(",")
following_old = []
for i in range (0,len(targelist)):
    count=0
    print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒',targelist[i],'▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
    profile = instaloader.Profile.from_username(L.context, targelist[i])
    # Print list of followees
    following_now = []
    for followee in profile.get_followees():
        following_now.append(followee.username)
        #file = open("prada_followers.txt", "a+")
        #file.write(follow_list[count])
        #file.write("\n")
        #file.close()
        count = count + 1
    print('folwing count for ',targelist[i],': ',len(following_now))
    if i != 0 :
        following_old = set.intersection(set(following_old),set(following_now))
    else:
        following_old=following_now

print("done press anykey to continu")
input("")
print(following_old)
'''
for i in range(0,len(following_old)):
    file = open("intersaelctdddssdddcxvxvxvxv.txt", "a+")
    file.write(following_old[i])
    file.write("\n")
    file.close()
print('by:)')

maorojloo=[]
count=0
print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒maorojloo▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒')
profile = instaloader.Profile.from_username(L.context, "ma.orojloo")
# Print list of followees
maorojloo = []
for followee in profile.get_followees():
    maorojloo.append(followee.username)
#file = open("prada_followers.txt", "a+")
#file.write(follow_list[count])
#file.write("\n")
#file.close()
    count = count + 1
print('folwing count for maorojloo: ',len(maorojloo))
mmd="kiri"

finala = set(following_old)-set(maorojloo)

print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print(finala)

'''

 

