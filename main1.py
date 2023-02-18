globsl_init(input())
session = create_session()
for user in session.query(User).filter(User.address == 'module_1', User.speciality.notlike('%engineer%'),
                                       User.position.notlike('%engineer%')).all():
    print(user.id)
