#example1
#If the user enters a value that cannot be converted to an integer, a ValueError will be raised. 
#The except block catches this exception and executes the code inside it
# # def ask_for_int():

# #     while True:
# #         try:
# #             result = int(input('please provdie number:'))
# #         except:
# #             print('whoops! that is not number')
# #             continue
# #         else:
# #             print('yes thank you')
# #             break 
# #         finally:
# #             print('end of try/except/finally')
# #             print('i will always run at the end')

# # ask_for_int()


#example 2

# # def divide(x,y):
# #     try:
# #         result = x/y
# #     except ZeroDivisionError:
# #         print("please change 'y' arguement to non zero value")
# #     except:
# #         print('something went wrong')
# #     else:
# #         print(f'your answer is {result}')
# #     finally:
# #         print('i am always gonna run')

# # divide(1,0)


#example 3

def file_editor(path,text):
    try:
        data = open(path)

        try:
            data.write(text)
        except:
            print("unable to write the text,Please add an append: 'a' or write: 'w' parameter to the open() function.")
        
        finally:
            data.close()
    except:
        print(f"{path} file not found")

path='data.txt'
text='hello expection handling with python'

file_editor(path,text)
