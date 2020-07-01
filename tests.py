from datetime import datetime
import unittest
from app import app, db
from app.models import User, Post


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        # Setting up db
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.create_all()

    def tearDown(self):
        # Deleting db
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(name="test user", email="test@email.com", password="pass")
        u.generate_password(u.password)
        self.assertFalse(u.check_password("notpass"))
        self.assertTrue(u.check_password("pass"))

    def test_avatar(self):
        u = User(name="test user", email="test@email.com", password="pass")
        self.assertEqual(
            u.avatar(64),
            "https://www.gravatar.com/avatar/93942e96f5acd83e2e047ad8fe03114d?s=64&d=identicon",
        )

    def test_follow(self):
        u = User(name="test user", email="test@email.com", password="pass")
        u2 = User(name="test user2", email="test2@email.com", password="pass")
        u3 = User(name="test user3", email="test3@email.com", password="pass")
        u.generate_password(u.password)
        u2.generate_password(u2.password)
        db.session.add_all([u, u2, u3])
        db.session.commit()
        u.follow(u2)
        self.assertEqual(u.is_following(u2), True)
        self.assertEqual(u.is_following(u3), False)

        u.unfollow(u2)
        self.assertFalse(u.is_following(u2))
        self.assertEqual(u.followed.count(), 0)
        self.assertEqual(u2.followed.count(), 0)

    def test_follow_posts(self):
        u = User(name="test user", email="test@email.com", password="pass")
        u2 = User(name="test user2", email="test2@email.com", password="pass")
        u3 = User(name="test user3", email="test3@email.com", password="pass")
        u.generate_password(u.password)
        u2.generate_password(u2.password)
        u3.generate_password(u3.password)
        db.session.add_all([u, u2, u3])
        u.follow(u2)
        p1 = Post(body="some text for a post", user_id=u2.id)
        p2 = Post(body="some text for another post", user_id=u2.id)
        db.session.add_all([p1, p2])
        db.session.commit()
        followed_post_count = len(list(u.followed_posts()))
        self.assertEqual(followed_post_count, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
