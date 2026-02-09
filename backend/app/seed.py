from sqlmodel import Session, select
from .models import User, Profile
from .auth import hash_password
from .settings import settings

def seed_admin(session: Session):
    existing = session.exec(select(User).where(User.email == settings.ADMIN_EMAIL)).first()
    if existing:
        return
    admin = User(
        email=settings.ADMIN_EMAIL,
        password_hash=hash_password(settings.ADMIN_PASSWORD),
        is_admin=True
    )
    session.add(admin)
    session.commit()
    session.refresh(admin)

    p = Profile(user_id=admin.id, name="Admin", is_kids=False)
    session.add(p)
    session.commit()
