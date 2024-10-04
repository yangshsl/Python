# x = 1
# y = 2
# z = 1.2

# print(x + y)
# print(x - y)
# print( x * y)
# print(x % y)
# print(x ** y)


# x = "hello"
# y = 'bye' 

# z = """
# 안녕하세요 
# 위니입니다."""

# print(z)

# print("너 혹시 몇살이니?" + str(4))

# x = 4
# y = "4"

# print(int(y) + x)

# x = True
# y = False

# print(x) 
# print(y)

# x = 3
# if x > 5:
#     print("Hello")
# elif x == 3:
#     print("Bye")
# else:
#     print("Hi")

# def chat(name1, name2, age):
#     print("%s: 안녕? 넌 몇살이니?" %name1)
#     print("%s: 나? 나는 %d" %(name2, age))

# chat("영희", "철수", 20)
# chat("우헤헤", "우히히", 20)

# def dsum(a, b):
#     result = a + b
#     return result
# d = dsum(2, 4)
# print(d)

# def sayHello(name, age):
#     if(age < 10):
#         print("안녕") 
#     elif (10 <= age <= 20):
#         print("안녕하세여")
#     else:
#         print("안녕하십니까")

# sayHello("세현", 18)


#for/ while
# for i in range(3):
#     print(i)
#     print("철수: 안녕 영희야 뭐해??")
#     print("영희: 안녕 철수야, 그냥 있어.")

# for i in range(100)
#     print(i) 
#     print("철수: 안녕 영희야 뭐해??")
#     print("영희: 안녕 철수야, 그냥 있어.")

#     continue
#     print("워니: 안녕 철수와 영희야!")
    

# x = [4, 3, 2, 1]
# y = ["hello", "there"]

# print("hello" in y)

# x = ('a', 'b', 'c')
# xz = (1, "hello", "there")
# print(z.index(1))

# x = dict()
# y = {}

# print(x)
# print(y)

# x = {"name": "워니",
#      "age": 20}

# print("name" in x)
# print(x.keys())
# print(x.values())

# for key in x:
#     print(key)
#     print(x[key])

fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

d = {}
for f in fruit:
    if f in d:
        d[f] = d[f]+1
    else:
        d[f] = 1

print(d)