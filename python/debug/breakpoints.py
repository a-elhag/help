import ipdb

dbg1 = ipdb.set_trace  # BREAKPOINT
for i in range(10):
    my_var2 = 10 / 3
    dbg1()  # BREAKPOINT
    dbg1 = lambda: None
    print(my_var2)


dbg2 = ipdb.set_trace  # BREAKPOINT
for i in range(10):
    my_var2 = 20 / 3
    dbg2()  # BREAKPOINT
    dbg2 = lambda: None
    print(my_var2)



# def f(): pass
# ipdb.set_trace = f

# ipdb.set_trace = lambda: None
