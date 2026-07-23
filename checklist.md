# 체크리스트

## 랜딩 index.html 뼈대 (2026-07-23)
- [x] shared/style.css — 모바일 우선 공통 스타일, --brand-color 변수
- [x] shared/i18n.js — JSON 로드 + data-i18n 치환 + 언어 토글 공통 모듈
- [x] shared/landing/{ko,en,zh}.json — 랜딩 번역 텍스트
- [x] index.html — 랜딩 뼈대 (방 링크 없음, 섹션 플레이스홀더)
- [x] 로컬 서버로 동작 확인 (전 리소스 200 확인)

## PDF 콘텐츠 반영 (2026-07-23)
- [x] shared/i18n.js — 다중 소스(공통+방별) JSON 병합 지원
- [x] shared/common/{ko,en,zh}.json — 분리수거, 이용 규칙, 비상연락처
- [x] g/v4qfqfbq/ — 방 페이지 + 방별 번역 JSON (와이파이, 출입, 가전, 주변, 교통, FAQ, 체크아웃)
- [x] 도어락 비밀번호 제외 확인 (grep 검사), doc/ .gitignore 처리
- [x] 랜딩 문구 실제 내용으로 교체
- [x] 검증 — JSON 파싱, 키 커버리지(98개), 리소스 200

## 다음 작업 (미착수)
- [ ] generator/ 방 추가 스크립트
- [ ] QR 코드 생성 (방 페이지 URL)
