from project import db


# TODO: setup association table
# class Username(db.Model):
#     __tablename__ = "username"
#     id = db.Column(
#         db.Integer, primary_key=True, autoincrement=True
#     )
#     user_id = db.Column(
#         db.Integer, db.ForeignKey("user.id"), nullable=False
#     )
#     users = db.relationship("")
#     username = db.Column(
#         db.String(128), index=True, unique=True, nullable=False
#     )

#     def __repr__(self):
#         return f"<Username {self.username}>"

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "username": self.username,
#         }