import praw
import webbrowser
from win10toast_click import ToastNotifier 

reddit = praw.Reddit(client_id = "",
                            client_secret = "",
                            username = "",
                            password = "",
                            user_agent = "")


subreddit = reddit.subreddit('worthy')
def open_url():
    webbrowser.open_new_tab(url1)

for submission in subreddit.stream.submissions(skip_existing=True):
    url1 = submission.url
    toaster = ToastNotifier()


    toaster.show_toast( #stolen right from docs lol
        "A new post appeared", # title
        "Click to open URL!", # message 
        icon_path=None, # 'icon_path' 
        duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
        callback_on_click=open_url # click notification to run function 
        )



