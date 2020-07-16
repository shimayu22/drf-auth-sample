# drf-auth-sample

Django REST FrameworkのJWT認証サンプル
DjangoModelPermissionsを使うことで、ユーザーに付与した権限の範囲でAPIを叩くことができる。

[Permissions](https://www.django-rest-framework.org/api-guide/permissions/)

## 初期設定

### Win版
    python -m venv env
    env\Sctipts\activate
    pip install -r requirements.txt
    manage.py migrate
    manage.py createsuperuser
    manage.py runserver

### Mac版
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

## 使い方
### 1.ユーザー登録
- Djangoの管理画面で「ユーザーを追加」からユーザーを作成する
- ユーザー名、パスワード入力後、「保存して編集を続ける」をクリック
- 「パーミッション」の「スタッフ権限」にチェックをつける（管理画面での動作確認用、APIだけで確認するなら不要)
- ユーザーパーミッションにて、「TODO」でフィルターをして各種権限を追加する
  - 前もってグループで設定しておき、グループを選択してもOK
- Postmanで「sample.postman_collection.json」をインポートする
- 「http://127.0.0.1:8000/api/token/」 タブでトークンを取得する
  - Bodyを適宜修正する
- 取得したアクセストークン("access": アクセストークン)をHeadersに設定する
  - KEY:Authorization
  - VALUE:Beaer アクセストークン
- BodyやURLのpkを修正しながら確認する

