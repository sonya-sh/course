import json


class Model:
    a = '1'
    b = '2'
    c = '3'

    def save(self):
        d = {}
        attr = list(filter(lambda x: not x.startswith('_'), dir(Model)))
        attr.remove('save')
        for i in attr:
            d[i] = eval('self.' + i)
        with open('file.json', 'w') as f:
            json.dump(d, f)
        return print(d)


test = Model()
test.a = '4'
test.b = '5'
test.c = '6'
test.save()
