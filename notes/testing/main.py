def do_stuff(num):
    try:
        return num + 5
    except TypeError as err:
        return err
