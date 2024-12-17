def f(shopping_cart,price_list,custommer_wallet):
    c=0
    for k,v in  shopping_cart.items():
        c+=price_list[k]*v
    if c>custommer_wallet:
        return False
    else:
        return True
if __name__=='__main__':
    print(f(shopping_cart={'juice':3, 'bread':1,'milk':2}, price_list={'milk':1.49,'butter':2.09,'juice':1.19,'bread':1.99}, custommer_wallet=10))
    print(f(shopping_cart={'juice':3, 'bread':1,'milk':2}, price_list={'milk':1.49,'butter':2.09,'juice':1.19,'bread':1.99}, custommer_wallet=8))


