
def input_get_input(self):

    _i = self.request.GET

    i = {
        'user' : self.request.user,
    }

    return i
