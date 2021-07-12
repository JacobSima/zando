def input_get_input(self):

    _i   = self.request.GET
    user = self.request.user

    i = {
        'user'          : user,
        'user_fullname' : user.fullname,

        'type'          : _i.get('type'),
        'assignee'      : _i.get('assignee'),
        'assigner'      : _i.get('assigner'),
    }

    return i
