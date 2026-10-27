#!/usr/bin/env python3
"""Оставляет в geosite.dat только нужные списки. Без зависимостей.
Использование: python3 trim_geosite.py geosite.dat geosite-small.dat
"""
import sys

KEEP = {
    # Списки для роутинга Happ и РФ (блокировки РКН, госсервисы, зоны РФ, локальные сети)
    "ru-blocked",
    "ru-available-only-inside",
    "category-ru",
    "private",

    # Блокировка рекламы и трекеров
    "category-ads-all",
    "win-spy",

    # Google и YouTube (для Xray / v2rayNG / rutest)
    "youtube",
    "google",

    # Популярные сервисы и соцсети
    "telegram",
    "discord",
    "tiktok",
    "instagram",
    "facebook",
    "twitter",
    "openai",
}


def read_varint(b, i):
    r = s = 0
    while True:
        c = b[i]
        i += 1
        r |= (c & 0x7F) << s
        if not c & 0x80:
            return r, i
        s += 7


def write_varint(n):
    out = bytearray()
    while True:
        c = n & 0x7F
        n >>= 7
        if n:
            out.append(c | 0x80)
        else:
            out.append(c)
            return bytes(out)


def main(src, dst):
    data = open(src, "rb").read()
    i, out, found = 0, bytearray(), set()
    while i < len(data):
        tag, i = read_varint(data, i)
        if tag != 0x0A:  # GeoSiteList.entry
            sys.exit(f"неожиданный тег {tag} на позиции {i}")
        ln, i = read_varint(data, i)
        entry = data[i:i + ln]
        i += ln
        t, j = read_varint(entry, 0)  # GeoSite.country_code
        if t != 0x0A:
            sys.exit("не найден country_code в записи")
        l, j = read_varint(entry, j)
        code = entry[j:j + l].decode().lower()
        if code in KEEP:
            out += b"\x0a" + write_varint(ln) + entry
            found.add(code)
    missing = KEEP - found
    if missing:
        sys.exit(f"в исходном файле нет списков: {sorted(missing)}")
    open(dst, "wb").write(out)
    print(f"ok: {len(data)/1e6:.1f} МБ -> {len(out)/1e6:.1f} МБ, списков: {len(found)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
