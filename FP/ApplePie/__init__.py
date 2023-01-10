from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


# creat_app는 플라스크 내부에서 정의된 함수명
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, auth_views, model_views
    
    # Main Page
    app.register_blueprint(main_views.bp)

    # 회원가입 인증
    app.register_blueprint(auth_views.bp)

    # 모델 도입
    app.register_blueprint(model_views.bp)

    return app