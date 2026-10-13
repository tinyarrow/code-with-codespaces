import random

def guess_the_number():
    print("=" * 35)
    print("🎮 欢迎来到 '猜数字' 小游戏！")
    print("我已经想好了一个 1 到 100 之间的数字。")
    print("=" * 35)
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\n请输入你猜的数字（还剩 {max_attempts - attempts} 次机会）: "))
            attempts += 1
            
            if guess < secret_number:
                print("📉 太小了！再试试。")
            elif guess > secret_number:
                print("📈 太大了！再试试。")
            else:
                print(f"\n🎉 太棒了！你在第 {attempts} 次猜中了！数字就是 {secret_number}。")
                return
        except ValueError:
            print("⚠️ 请输入有效的数字！")
            
    print(f"\n💀 很遗憾，次数用完了。正确答案是 {secret_number}。")

if __name__ == "__main__":
    guess_the_number()