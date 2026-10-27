# geo-trim

Оптимизированные файлы `geosite.dat` и `geoip.dat` для клиентов Xray / Happ / v2rayNG / Sing-box с быстрой доставкой через jsDelivr CDN.

## Описание
Оригинальный файл `geosite.dat` из репозитория `russia-v2ray-rules-dat` превышает 70 МБ, из-за чего бесплатный CDN jsDelivr отказывается его отдавать (жёсткий лимит jsDelivr — 20 МБ на файл).

Скрипт `trim_geosite.py` извлекает только те списки, которые используются в правилах маршрутизации (РКН, госсервисы, баннеры/телеметрия, популярные стриминги и соцсети), сокращая вес файла до ~5.5 МБ.

Базы автоматически обновляются каждые 6 часов с помощью GitHub Actions.

## Прямые ссылки (jsDelivr CDN)

- **geosite.dat**:
  ```text
  https://cdn.jsdelivr.net/gh/TheNotus/geo-trim@main/geosite.dat
  ```
- **geoip.dat**:
  ```text
  https://cdn.jsdelivr.net/gh/TheNotus/geo-trim@main/geoip.dat
  ```

## Включённые теги geosite
- `ru-blocked`
- `ru-available-only-inside`
- `category-ru`
- `private`
- `category-ads-all`
- `win-spy`
- `youtube`
- `google`
- `telegram`
- `discord`
- `tiktok`
- `instagram`
- `facebook`
- `twitter`
- `openai`
