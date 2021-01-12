#decorator


def sub_dec(func):
    def wrap(n1,n2):
        if n1 < n2:
            n1,n2=n2,n1
        return func(n1,n2)

    return wrap


@sub_dec
def sub(num1,num2):

    return num1-num2

res=sub(40,50)
print(res)