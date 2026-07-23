# 새 방 페이지(슬러그 폴더, 번역 JSON, QR, 인쇄 안내판)를 한 번에 생성하는 스크립트
#
# 사용법 (저장소 루트에서 실행):
#   python generator/new_room.py                # 기본 템플릿(v4qfqfbq)을 복사해 새 방 생성
#   python generator/new_room.py --from 슬러그  # 다른 방을 템플릿으로 사용
#
# 필요 패키지: pip install "qrcode[pil]"
# 생성 후 새 방의 ko/en/zh.json에서 방별 정보(와이파이, 위치 등)를 수정하세요.

import argparse
import re
import secrets
import shutil
import string
import sys
from pathlib import Path

# Windows 콘솔(cp949)에서 한글 출력이 깨지지 않도록 UTF-8로 강제
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_URL = "https://castlesix.github.io/lalastay-guide"
DEFAULT_TEMPLATE = "v4qfqfbq"
SLUG_CHARS = string.ascii_lowercase + string.digits
SLUG_LEN = 8

ROOT = Path(__file__).resolve().parent.parent
ROOMS_DIR = ROOT / "g"


def make_slug() -> str:
    while True:
        slug = "".join(secrets.choice(SLUG_CHARS) for _ in range(SLUG_LEN))
        if not (ROOMS_DIR / slug).exists():
            return slug


def make_qr(url: str, out_dir: Path) -> None:
    try:
        import qrcode
        import qrcode.image.svg
    except ImportError:
        sys.exit('qrcode 패키지가 필요합니다. 먼저 실행하세요: pip install "qrcode[pil]"')

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(out_dir / "qr.png")

    qr_svg = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=4,
                           image_factory=qrcode.image.svg.SvgPathImage)
    qr_svg.add_data(url)
    qr_svg.make(fit=True)
    qr_svg.make_image().save(out_dir / "qr.svg")


def main() -> None:
    parser = argparse.ArgumentParser(description="새 방 페이지 생성")
    parser.add_argument("--from", dest="template", default=DEFAULT_TEMPLATE,
                        help=f"템플릿으로 복사할 기존 방 슬러그 (기본: {DEFAULT_TEMPLATE})")
    parser.add_argument("--base-url", default=BASE_URL, help="배포 기본 URL")
    args = parser.parse_args()

    src = ROOMS_DIR / args.template
    if not src.is_dir():
        sys.exit(f"템플릿 방을 찾을 수 없습니다: {src}")

    slug = make_slug()
    dst = ROOMS_DIR / slug
    dst.mkdir(parents=True)

    for name in ["index.html", "ko.json", "en.json", "zh.json"]:
        if not (src / name).exists():
            sys.exit(f"템플릿에 {name}이 없습니다: {src / name}")
        shutil.copy(src / name, dst / name)

    url = f"{args.base_url}/g/{slug}/"
    make_qr(url, dst)

    print_src = src / "print.html"
    if print_src.exists():
        html = print_src.read_text(encoding="utf-8")
        html = re.sub(rf"\bg/{re.escape(args.template)}/", f"g/{slug}/", html)
        (dst / "print.html").write_text(html, encoding="utf-8")

    print(f"생성 완료: g/{slug}/")
    print(f"  페이지    : {url}")
    print(f"  안내판    : {url}print.html")
    print(f"  QR        : qr.png / qr.svg")
    print()
    print("다음 단계.")
    print(f"  1. g/{slug}/ko.json, en.json, zh.json에서 방별 정보(와이파이 등)를 수정하세요.")
    print("  2. 커밋 후 푸시하면 GitHub Pages에 배포됩니다.")


if __name__ == "__main__":
    main()
