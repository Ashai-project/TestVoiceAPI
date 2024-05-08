# 準備
- step1
  - GoogleCloudにアカウント登録
- step2
  - プロジェクト新規作成

  - APIとサービス->ライブラリからSpeach to textを検索、プロジェクトに追加
- step3
  - IAMと管理->サービスアカウントから新規サービスアカウントの追加

  - キーの発行

- step4
  - 作成したキーファイルのパスを環境変数に設定

  - 変数名:GOOGLE_APPLICATION_CREDENTIALS

# 実行方法
動作確認:Python 3.12.3

必要なライブラリのインストールをしてください
```
pip install {$Library}
```

入力は.wavのみステレオ音源はモノラル音源に変更してください
```
Python　wavefile_stereo2mono.py
```


