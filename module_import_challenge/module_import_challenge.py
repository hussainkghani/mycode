#!/usr/bin/env python3
import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

question = print(trivia["question"])

correct_answer = print(trivia["correct_answer"])

incorrect_answer1 = print(trivia(html.unescape["incorrect_answers"][0]))

incorrect_answer2 = print(trivia["incorrect_answers"][1])

incorrect_answer3 = print(trivia["incorrect_answers"][2])


