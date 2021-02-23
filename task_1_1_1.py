sec_list = [1548, 5630, 12960, 25870, 36810]
for seconds in sec_list:
    ss = seconds % 60
    minutes = seconds // 60
    mm = minutes % 60
    hours = minutes // 60
    hh = hours % 24
    dd = hours // 24

    print("%02d:%02d:%02d:%02d" % (dd, hh, mm, ss))
