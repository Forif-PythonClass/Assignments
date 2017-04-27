money=0
coke=0
juice=0
energydrink=0
while(money<10000):
    menu = input()
    if menu=="coke":
        money=money+1500
        coke=coke+1
    elif menu=="juice":
        money=money+1200
        juice=juice+1
    elif menu == "energy drink":
        money = money + 2000
        energydrink=energydrink+1
print("총 :{}원\nCoke {}개\nJuice {}개\nEnergy Drink {}개\n".format(money,coke,juice,energydrink))
