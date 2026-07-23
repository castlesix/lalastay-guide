# 컨텍스트 노트

## 2026-07-23 — 랜딩 뼈대 + i18n 기반
- 루트 index.html은 CLAUDE.md 규칙대로 방 링크 없는 랜딩만. 섹션은 환영 인사 / 이용 안내 / 문의 3개 플레이스홀더.
- 번역 텍스트는 HTML에 하드코딩하지 않고 `data-i18n="키"` 속성 + JSON으로 분리. 랜딩 번역은 `shared/landing/{ko,en,zh}.json`에 둠 (방별 번역은 나중에 `g/{슬러그}/{lang}.json`).
- `shared/i18n.js`는 범용 모듈. `I18N.init({ basePath })`로 JSON 위치만 넘기면 랜딩/방 페이지 어디서든 재사용 가능. 언어 선택은 localStorage(`lalastay-lang`)에 저장, 없으면 navigator.language로 감지(ko/en/zh 외에는 en).
- JSON을 fetch로 로드하므로 file:// 로 직접 열면 동작하지 않음. 로컬 확인은 `python -m http.server` 등 정적 서버 필요. GitHub Pages에서는 문제 없음.
- 브랜드 컬러는 `shared/style.css`의 `:root { --brand-color }` 한 곳에서만 관리. 따뜻한 톤으로 임시 지정, 확정 컬러 나오면 이 변수만 교체.
