# Lala Stay Guest Guide

라라스테이 숙박 게스트용 다국어(한/영/중) 홈 가이드 정적 사이트.

## 브랜딩
- 표기: Lala Stay (영문) / 라라스테이 (국문) / 중문은 Lala Stay 그대로
- 페이지 타이틀·헤더에 브랜드명 노출, 톤은 따뜻하고 심플하게
- 브랜드 컬러는 :root CSS 변수(--brand-color)로만 관리

## 기술 스택
- 순수 HTML/CSS/JS, 빌드 도구 없음
- 호스팅: GitHub Pages, 모바일 우선(QR 스캔 접근)

## 구조
- shared/ : style.css, i18n.js, 공통 콘텐츠(쓰레기 배출, 비상연락처)
- g/{랜덤슬러그}/ : 방별 페이지 (index.html + ko/en/zh.json)
- generator/ : 방 추가 스크립트
- 루트 index.html은 랜딩만, 방 링크 노출 금지

## 규칙
- 방 식별자는 8자리 랜덤 슬러그 (room101 같은 추측 가능한 이름 금지)
- 도어락 비밀번호는 절대 페이지에 포함하지 않음
- 번역 텍스트는 JSON 분리, HTML에 하드코딩 금지
- 외부 CDN 의존 최소화
- 공통 콘텐츠는 shared에서 로드, 방별 차이만 방 JSON에