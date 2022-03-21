n_ps =input("введите пароль")
ps = input("введите пароль")
def ask_password(ps_f,n_ps_f):
    run = True
    while run :
        if ps_f == n_ps_f:
            print("пароль принят")
            run = False
        else:
            print("в доступе отказано")
            run = False
ask_password(ps,n_ps)







