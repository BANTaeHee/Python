'''
    순신은 lily라는 이름의 교환학생과 친해지게 되었습니다.
    영어를 잘하지 못하는 순신은 lily에게 한국어를 가르쳐 주기 위해
    한국어 연습 프로그램을 만들게 되었습니다.
        - 연습할 한국어가 담긴 리스트를 만든다.
        - 리스트에서 순서대로 단어를 가져와 화면에 출력한다.
        - 프로그램 사용자는 단어를 그대로 입력한다


    Ex.
        Let's learning Korean
        사랑해
        사랑해
        귀여워
        귀여워
        고마워
        고마워
        행복해
        행복해
'''

words = ["사랑해", "귀여워", "고마워", "행복해"]
score = 0       # 점수

print("올바른 정답을 답하세요")

for word in words:
    print(word)

    A = input()

    #if A != word:
     #   print("틀렸습니다. 다시 생각해보세요!")
      #  break

   if A == word:
       score += 1
# 전체 문제 개수 : 4개             len(word_list)
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개

print("전체 문제 개수 : ", len(words))
print("맞힌 문제 개수 : ", score)
print("틀린 문제 개수 : ", len(words) - score, "개")