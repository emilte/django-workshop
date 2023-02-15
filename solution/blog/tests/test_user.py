from blog.models import User


def test_create_user():
    test_username = 'test'

    user: User = User.objects.create_superuser(username=test_username)
    assert user.username == test_username
    assert user.is_superuser is True
