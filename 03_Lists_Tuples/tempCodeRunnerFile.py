print("Timing")
    x = timeit.timeit("sanitise_1(data_list1)",
                      setup="from __main__ import sanitise_1,"
                            "data_list1",
                      number=1)
    print("{:15.15f}".format(x))
    y = timeit.timeit("sanitise_2(data_list2)",
                      setup="from __main__ import sanitise_2,"
                            "data_list2",
                      number=1)
    print("{:15.15f}".format(y))
    z = timeit.timeit("sanitise_3(data_list3)",
                      setup="from __main__ import sanitise_3,"
                            "data_list3",
                      number=1)
    print("{:15.15f}".format(z))