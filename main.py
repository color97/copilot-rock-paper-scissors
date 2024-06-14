# 导入random模块
import random

# 定义主函数，处理所有逻辑
def main():
    # 创建可能的选择列表
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    # 显示选项列表
    print("Choose your option:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    # 获取用户输入
    user_choice = int(input('Enter the number of your choice: '))
    # 获取计算机选择
    computer_choice = random.choice(choices)
    # 打印计算机选择
    print(f'Computer choice: {computer_choice}')
    # 确定赢家
    if choices[user_choice-1] == computer_choice:
        print('It\'s a tie!')
    elif (choices[user_choice-1] == 'rock' and (computer_choice in ['scissors', 'lizard'])) or \
         (choices[user_choice-1] == 'paper' and (computer_choice in ['rock', 'spock'])) or \
         (choices[user_choice-1] == 'scissors' and (computer_choice in ['paper', 'lizard'])) or \
         (choices[user_choice-1] == 'lizard' and (computer_choice in ['paper', 'spock'])) or \
         (choices[user_choice-1] == 'spock' and (computer_choice in ['rock', 'scissors'])):
        print('You win!')
    else:
        print('You lose!')

# 调用主函数
main()