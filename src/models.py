from src import db
from flask import jsonify


class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    testname = db.Column(db.String(80), unique=True, nullable=False)

    session = db.session

    def to_dict(self):
        return {
            "id" : self.id,
            "testname" : self.testname
            }

    def get_test(params):
        get_test = Test.session.query(Test).filter_by(**params).all()
        return build_output(get_test)

    def create_test(params):
        try_test= Test(**params)
        Test.session.add(try_test)
        Test.session.commit()
        get_test = Test.get_test(try_test.to_dict())
        return get_test
