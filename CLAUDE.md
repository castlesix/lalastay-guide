# Lala Stay Guest Guide

라라스테이 숙박 게스트용 다국어(한/영/중) 홈 가이드 정적 사이트.

## 브랜딩
- 표기: Lala Stay (영문) / 라라스테이 (국문) / 중문은 Lala Stay 그대로
- 페이지 타이틀·헤더에 브랜드명 노출, 톤은 따뜻하고 심플하게
- 브랜드 컬러는 :root CSS 변수(--brand-color)로만 관리

## 기술 스택
- 순수 HTML/CSS/JS, 빌드 도구 없음
- 호스팅: GitHub Pages, 모바일 우선(QR 스캔 접근)
- 배포: main 브랜치 푸시 시 자동 배포 → https://castlesix.github.io/lalastay-guide/

## 구조
- shared/ : style.css, i18n.js, landing/(랜딩 번역), common/(공통 번역 — 분리수거·이용 규칙·비상연락처)
- g/{랜덤슬러그}/ : 방별 페이지 (index.html, ko/en/zh.json, qr.png/svg, print.html 인쇄 안내판)
- generator/new_room.py : 방 추가 스크립트 (슬러그 생성 + 템플릿 복사 + QR + 안내판 일괄 처리)
- doc/ : 원본 가이드 PDF — 도어락 비밀번호 포함이므로 .gitignore로 커밋 제외
- 루트 index.html은 랜딩만, 방 링크 노출 금지
- 방 페이지는 shared/common과 방 JSON을 병합해 렌더링 (I18N.init sources 옵션)

## 규칙
- 방 식별자는 8자리 랜덤 슬러그 (room101 같은 추측 가능한 이름 금지)
- 도어락 비밀번호는 절대 페이지에 포함하지 않음
- 번역 텍스트는 JSON 분리, HTML에 하드코딩 금지 (예외: print.html은 3개 언어 동시 표기 인쇄물이라 하드코딩 허용)
- 외부 CDN 의존 최소화
- 공통 콘텐츠는 shared에서 로드, 방별 차이만 방 JSON에