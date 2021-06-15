from app import db

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    twitter = db.Column(db.String(120), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)

    user_info = db.Column(db.Text)
    image = db.Column(db.String(250))
    description = db.Column(db.Text)


    def __init__(
        self,
        title,
        twitter="@arturoverbel",
        user_info="User Info",
        image="image.png",
        description="Desssss",
    ):
        self.title = title
        self.twitter = twitter

        self.description = description
        self.image = image
        self.user_info = user_info


    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def create(self):
        print("Creating...")
        results = db.session.query(Profile).filter(Profile.twitter == self.twitter).all()
        if len(results) > 0:
            return self.update()

        db.session.add(self)
        db.session.commit()

        return self.to_dict()

    def update(self):
        print("Updating...")
        results = db.session.query(Profile).filter(Profile.twitter == self.twitter).all()
        if len(results) < 1:
            return self.create()

        db.session.query(Profile).filter(Profile.twitter == self.twitter).update({
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'user_info': self.user_info,
        })
        db.session.commit()

        return self.to_dict()

    @staticmethod
    def delete(twitter):
        print("Deleting...")

        profile = db.session.query(Profile).filter(Profile.twitter == twitter).one()
        db.session.delete(profile)
        db.session.commit()

        return True

    @staticmethod
    def get(twitter):
        print("Getting...")
        result = db.session.query(Profile).filter(Profile.twitter == twitter).one()

        return result.to_dict()

    @staticmethod
    def get_last(limit=10):
        print("Getting last...")
        results = db.session.query(Profile).order_by(Profile.id.desc()).limit(limit).all()

        results_dict = [r.to_dict() for r in results]
        return results_dict
