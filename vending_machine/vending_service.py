balance=0
drinks=[
    {'name':'可樂','price':20},
    {'name':"雪碧",'price':20},
    {'name':'茶裏王','price':25},
    {'name':'原萃','price':25},
    {'name':'純粹喝','price':30},
    {'name':'水','price':20}
]
def add(x,y):
    '''
    數字相加
    :param x: 數字1
    :param y: 數字2
    :return: 相加結果
    '''
def deposit():
    '''
    儲值功能
    :return: nothing
    '''
    global  balance
    value = eval(input('儲值金額:'))
    while value < 1:
        # 若使用者輸入數字小於零 需要重新輸入
        print("====儲值金額需大於零")
        value = eval(input('儲值金額:'))
    balance += value
    print(f'儲值後餘額為{balance}元')

def buy():
    global  balance,drinks
    print('\n請選擇商品')
    for i in range(0, len(drinks)):
        print(f'({i+1})\t{drinks[i]["name"]} \t {drinks[i]["price"]}元')
    choose = eval(input('請選擇編號'))

    while choose < 1 or choose > 6:
        print('請輸入1-6之間')
        choose = eval(input('請選擇:'))

    buy_drink = drinks[choose - 1]
    while balance < buy_drink['price']:
        print('====餘額不足，需要儲值嗎?')
        want_deposit=input('y/n')
        if want_deposit=='y':
            deposit()
        elif want_deposit=='n':
            break
        else:
            print('===請重新輸入====')
    #儲值後餘額大於商品再購買
    if balance >=buy_drink['price']:
        print(f'已購買{buy_drink["name"]} {buy_drink["price"]}元')
        balance-=buy_drink['price']
        print(f'購買後餘額為{balance}元')