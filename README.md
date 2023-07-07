# demo-streamlit-langchain

LangChain を Streamlit 上で動かすデモアプリ

## Deploy

## Running Locally

**1. Clone Repo**

```bash
git clone # FIXME
```

**2. Install Dependencies**

```bash
poetry install
```

**3. Provide OpenAI API Key**

Create a .env.local file in the root of the repo with Env:

```bash
OPENAI_API_KEY=""
# ..snip..
```

**4. Run App**

```bash
poetry shell
streamlit run home.py
```

**5. Use It**

You should be able to start chatting.

## Running Cloud Run

**1. Clone Repo**

```bash
git clone # FIXME
```

**2. Install Dependencies**

```bash
poetry install
```

**3. Prepare Google Cloud**

Authenticate and switch projects.

```bash
gcloud auth login
gcloud projects list
gcloud config set project <your-project-id>
```

Enable Services.

```bash
gcloud services enable compute.googleapis.com run.googleapis.com \
    artifactregistry.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com
```

**4. Set Secrets**

Create secrets and add their values.

```bash
# シークレット作成
gcloud secrets create OPENAI_API_KEY --replication-policy="automatic"

# 値を設定
echo -n "sk-xxx" | gcloud secrets versions add OPENAI_API_KEY --data-file=-

# Service account を確認
gcloud run services describe demo-streamlit-langchain --platform managed --region asia-northeast1

# Cloud Run にシークレットへのアクセスを許可する。SERVICE_ACCOUNT_EMAIL は上記で確認した Service account に置き換え。
gcloud secrets add-iam-policy-binding OPENAI_API_KEY \
  --member='serviceAccount:SERVICE_ACCOUNT_EMAIL' \
  --role='roles/secretmanager.secretAccessor'

# 必要に応じて他のシークレットも同様に設定
```

**5. Run App**

Deploy.

```bash
gcloud run deploy demo-streamlit-langchain --region "asia-northeast1" --source . \
    --allow-unauthenticated --quiet --update-secrets=OPENAI_API_KEY=OPENAI_API_KEY:latest
```

refs: https://zenn.dev/google_cloud_jp/articles/streamlit-01-hello

## 参考

認証機能が提供されていないので、デプロイする際は、デプロイ先のセキュリティサービス or サードパーティのモジュールを利用推奨。

- https://zenn.dev/google_cloud_jp/articles/streamlit-02-firebase
- https://zenn.dev/matken/articles/restrict-cloud-run-to-in-house
- https://github.com/mkhorasani/Streamlit-Authenticator
