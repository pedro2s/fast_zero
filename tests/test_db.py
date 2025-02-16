from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='alice', email='alice@example.com', password='senha123'
    )

    session.add(user)
    session.commit()
    # session.refresh(user)

    result = session.scalar(
        select(User).where(User.email == 'alice@example.com')
    )

    assert result.username == 'alice'
