# import logging.config
#
# from src.ecgai_logging.log_decorator import log
# from src.example.my_class import MyClass
#
# logging.config.fileConfig('logging.conf')
#
# # create logger
# logger = logging.getLogger(__name__)
#
#
# @log
# def number(a, b, c):
#     d = a * b * c
#     return d
#
#
# @log
# def divide_by_zero(a, b, c):
#     d = 0 / 0
#     return d
#
#
# @log
# def return_three_numbers(a: int, b: int, c: int):
#     return c, b, a
#
#
# @log
# def print_hi():
#     print('')
#     # Use a breakpoint in the code line below to debug your script.
#     # print(f'Hi, {name}')
#     # # 'application' code
#     # logger.debug('debug message')
#     # logger.info('info message')
#     # logger.warning('warn message')
#     # logger.error('error message')
#     # sleep(1)
#     # logger.critical('critical message')
#     # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     my = MyClass()
#     j, k, m = my.just_testing(2, 4, 6)
#     p, q, r = my.just_testing2(45454, 55884654, 656664)
#     y = my.just_testing3(2, 4, 6)
#     my.just_testing4(2, 4, 6)
#     my.just_testing5(2, 4, 6)
#     my.just_testing6(2, 4, 6)
#     my.just_testing9(9)
#     # my.just_testing10(9)
#     # print(f'result {j}, {k}, {m}')
#     # just_another_test(2, 5, 7)
#     # #
#     # d, e, f = return_three_numbers(25, 45, 21)
#     # # divide_by_zero(4,6,5)
#     # print({d}, {e}, {f})
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
