#!/bin/bash
# 教材管理模块部署脚本
# 将 courses_app 安装到 OJ 后端容器中

set -e
CONTAINER="onlinejudgedeploy-oj-backend-1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP_NAME="courses_app"

echo "=== Step 1: Copy Django app to container ==="
docker cp "$SCRIPT_DIR" "$CONTAINER:/app/$APP_NAME"

echo "=== Step 2: Ensure data directory exists ==="
docker exec "$CONTAINER" mkdir -p /app/data

echo "=== Step 3: Register app in Django settings ==="
docker exec "$CONTAINER" sh -c "
    if ! grep -q \"'$APP_NAME',\" /app/oj/settings.py; then
        sed -i \"/'grouping',/a\\    '$APP_NAME',\" /app/oj/settings.py
        echo '  [OK] Registered $APP_NAME in INSTALLED_APPS'
    else
        echo '  [SKIP] $APP_NAME already registered'
    fi
"

echo "=== Step 4: Register admin URL routes ==="
docker exec "$CONTAINER" sh -c "
    if ! grep -q '$APP_NAME.urls_admin' /app/oj/urls.py; then
        sed -i \"/url(r\\\"\\^api\/admin\/\\\", include(\\\"grouping.urls\\\")),/a\\    url(r\\\"^api/admin/\\\", include(\\\"$APP_NAME.urls\\\")),\" /app/oj/urls.py
        echo '  [OK] Registered admin URLs'
    else
        echo '  [SKIP] Admin URLs already registered'
    fi
"

echo "=== Step 5: Register public URL routes ==="
docker exec "$CONTAINER" sh -c "
    if ! grep -q '$APP_NAME.urls_public' /app/oj/urls.py; then
        sed -i \"/url(r\\\"\\^api\/\\\", include(\\\"contest.urls.oj\\\")),/a\\    url(r\\\"^api/\\\", include(\\\"$APP_NAME.urls_public\\\")),\" /app/oj/urls.py
        echo '  [OK] Registered public URLs'
    else
        echo '  [SKIP] Public URLs already registered'
    fi
"

echo "=== Step 6: Initialize config file if not exists ==="
docker exec "$CONTAINER" python3 -c "
import json, os
path = '/app/data/groups_config.json'
if not os.path.exists(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump({'courses': []}, f, ensure_ascii=False, indent=2)
    print('  [OK] Created groups_config.json')
else:
    print('  [SKIP] groups_config.json already exists')
"

echo "=== Step 6b: Fix permissions (gunicorn runs as server:spj) ==="
docker exec "$CONTAINER" sh -c "
    chown -R server:spj /app/data/ 2>/dev/null || true
    chmod -R 755 /app/data/ 2>/dev/null || true
    echo '  [OK] Permissions fixed'
"

echo "=== Step 7: Restart backend ==="
docker restart "$CONTAINER"
echo "Waiting for backend to start (20s)..."
sleep 20

echo "=== Deployment complete! ==="
echo ""
echo "Verify: curl http://localhost/api/courses/"
