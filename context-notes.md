# 컨텍스트 노트

## 2026-07-23 — 랜딩 뼈대 + i18n 기반
- 루트 index.html은 CLAUDE.md 규칙대로 방 링크 없는 랜딩만. 섹션은 환영 인사 / 이용 안내 / 문의 3개 플레이스홀더.
- 번역 텍스트는 HTML에 하드코딩하지 않고 `data-i18n="키"` 속성 + JSON으로 분리. 랜딩 번역은 `shared/landing/{ko,en,zh}.json`에 둠 (방별 번역은 나중에 `g/{슬러그}/{lang}.json`).
- `shared/i18n.js`는 범용 모듈. `I18N.init({ basePath })`로 JSON 위치만 넘기면 랜딩/방 페이지 어디서든 재사용 가능. 언어 선택은 localStorage(`lalastay-lang`)에 저장, 없으면 navigator.language로 감지(ko/en/zh 외에는 en).
- JSON을 fetch로 로드하므로 file:// 로 직접 열면 동작하지 않음. 로컬 확인은 `python -m http.server` 등 정적 서버 필요. GitHub Pages에서는 문제 없음.
- 브랜드 컬러는 `shared/style.css`의 `:root { --brand-color }` 한 곳에서만 관리. 따뜻한 톤으로 임시 지정, 확정 컬러 나오면 이 변수만 교체.

## 2026-07-23 — PDF 기반 가이드 콘텐츠 반영
- doc/의 홈가이드 PDF(국문/영문)를 기반으로 첫 방 페이지 `g/v4qfqfbq/` 작성. 중문은 PDF에 없어 국문 기준으로 번역해서 작성함.
- 도어락 비밀번호(PDF에 있음)는 CLAUDE.md 규칙대로 페이지에 넣지 않고 "예약 메시지로 별도 안내" 문구로 대체. 체크아웃 안내의 "원래 비밀번호로 되돌리기"도 숫자 없이 표현. `grep 2089`로 미포함 검증.
- doc/ 폴더는 비밀번호가 포함된 원본이라 .gitignore로 커밋 제외.
- `I18N.init({ sources: [a, b] })`로 확장 — 여러 JSON을 fetch 후 Object.assign으로 병합(뒤가 우선). 방 페이지는 `['../../shared/common', '.']` 순서로 로드. 기존 basePath 옵션도 호환 유지(랜딩에서 사용 중).
- 콘텐츠 분리 기준 — 분리수거·이용 규칙·비상연락처는 shared/common에, 와이파이·출입·가전·주변·교통·FAQ·체크아웃은 방 JSON에. 호스트 카카오톡 ID는 전 방 공통이라 common에 둠.
- 인덕션 버튼 설명표는 표 대신 핵심 불릿(전원 1.5초, 20초 자동꺼짐, 타이머 1~60분, 차일드락 3초, H 잔열 표시)으로 정리.
