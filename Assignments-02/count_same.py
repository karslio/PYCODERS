data = "There are many variations or passages of Lorem Ipsum available," \
       " but the majority have suffered alteration in some Form, by injected humor," \
       " or randomized words which don't look equally believable. If you are going" \
       " to use a Passage of Lorem  Ipsum, you Need to be sure there isn't anything " \
       "embarrassing All in the middle of text All the Lorem Ipsum generators on the " \
       "Internet tend to repeat predefined chunks as necessary, making this the first " \
       "true generator on the Internet.  or over 200 Latin words, combined with a handful " \
       "of model Sentence structures, to Generate Lorem Ipsum which looks reasonable. The " \
       "generated Lorem Ipsum is therefore always free from repetition, injected humor, or " \
       "non-characteristic words etc."
newData = data.upper()
dictionary = {key: newData.count(key) for key in newData}
print(dictionary)
