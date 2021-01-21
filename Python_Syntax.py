# missing handle for the data
def harmonize(profile): # <- change the name to something more intuitive / changed profile_id to profile
    """Return list of emails in profile""" # <- we could complete the missing information on arguments and returns
    
    emails = profile['email'] 
    if not emails:
        emails = ''
    
    for document in profile.get('document', []):
       emails.extend(document.get('address', {}).get('email', []))
    
    emails = list(set(filter(None, emails)))
    print('email done')
    return {'email': emails}
# function is not being called
# this excercise was really confusing since i hadn't worked with python for a while, after reviewing a course called "writing functions in python" this were the things i could point out
# thought aboout using the regex library but without a provided file it was hard to do.