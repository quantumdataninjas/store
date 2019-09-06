# from project import db


# class Email(db.Model):
#     __tablename__ = "emails"
#     id = db.Column(
#         db.BigInteger, primary_key=True, autoincrement=True
#     )
#     simple_user_id = db.Column(
#         db.BigInteger, db.ForeignKey("simple_user.id"), nullable=False
#     )
#     user_id = db.Column(
#         db.BigInteger, db.ForeignKey("user.id")
#     )
#     email = db.Column(
#         db.String(128), index=True, unique=True, nullable=False
#     )

#     def __repr__(self):
#         return f"<Email {self.email}>"

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "email": self.email,
#         }
