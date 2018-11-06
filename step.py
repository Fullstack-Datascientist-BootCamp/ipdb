def subroutine(x, y):

    return x*y

def wrapper(x):
    # now you are here. press c
    return x

if __name__ == "__main__":
    a = 3
    b = 5
    # put break point on line 14 and 16
    # press "s"
    import ipdb; ipdb.set_trace() # BREAKPOINT
    subroutine(wrapper(a), b)
    import ipdb; ipdb.set_trace() # BREAKPOINT
    # press s then n 
    subroutine(
            a,b 
    )
    # You did not step in! press q to quit. Next time press s and s 
    subroutine(a,b)
