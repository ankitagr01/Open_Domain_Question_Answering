flag = True
while flag:
    print('-------------------------------------------------------------------------------------------')
    with open('test.txt') as f:
        lines = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    lines = [x.strip() for x in lines]
    i = 1
    for line in lines:


        print('Enter any character for next question')
        char = input()
        if char:
            continue
'''
while 1:    
    print('-------------------------------------------------------------------------------------------')
    user_story_inp = '.'
    print('Please input a query')
    user_query_inp = input().split(' ')
    user_story, user_query, user_ans = vectorize_stories([[user_story_inp, user_query_inp, '.']], word_idx,
                                                         story_maxlen, query_maxlen)
    user_prediction = model.predict([user_story, user_query])
    user_prediction = idx_word[np.argmax(user_prediction)]
    print('Result:')
    print(' '.join(user_query_inp), '| Prediction:', user_prediction)


'''