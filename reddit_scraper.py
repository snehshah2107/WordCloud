import praw
import json
import sys

def scrape_subreddit(name, **args):
    """
    takesh name of the subreddit as argument
    scrapes the subreddit for the sumissions in new posts and add it to the CSV
    to feed it to the subredditcloud
    """
    reddit = praw.Reddit(client_id='AtKSqjRN4jf8Rw',
                        client_secret='AzV_M2PY8OPp6rsIKTnhND5JR8U',
                        password='2107@Sneh',
                        user_agent='testscript by /u/axiousavocado',
                        username='AnxiousAvocado2107')

    subreddit = reddit.subreddit(name)
    submission_count = 0
    print('Scrapping the subreddit for data...')
    #open a file with write permission
    with open(subreddit.display_name+'-data.csv', 'w') as f:
    #     if len(sys.argv)>2:
    #         start = sys.argv[2]
    #         end = sys.argv[3]
    # #get start and end epoch time from users as arg 2,3
    #     else:
    # #if not default a time to scrape posts
    #         start = 1514808000 #Jan 1st 2018
    #         end = 1525176000 #May 1st 2018
    #write the self text of the submissions stream from subreddit posts to the file
        for submission in subreddit.hot(limit=2000):
            f.write(submission.selftext)
            submission_count +=1

        f.close()
    # Information for user 
    print('/r/' + name, 'submission count: ' + str(submission_count) +' added to the file')

if __name__=='__main__':
    if(len(sys.argv)>1):
        subreddit_name = sys.argv[1]
        scrape_subreddit(subreddit_name)
    else:    
        subreddit_name = input('Please enter a subreddit name :')
        scrape_subreddit(subreddit_name)

    