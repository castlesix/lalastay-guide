// 언어별 JSON을 불러와 data-i18n 요소에 텍스트를 채우는 공통 다국어 모듈
const I18N = (function () {
  const LANGS = ['ko', 'en', 'zh'];
  const STORAGE_KEY = 'lalastay-lang';
  let sources = ['.'];

  function detectLang() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (LANGS.includes(saved)) return saved;
    const nav = (navigator.language || 'ko').slice(0, 2);
    return LANGS.includes(nav) ? nav : 'en';
  }

  function applyDict(dict) {
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      const key = el.getAttribute('data-i18n');
      if (dict[key] !== undefined) el.textContent = dict[key];
    });
  }

  function markActive(lang) {
    document.querySelectorAll('.lang-toggle [data-lang]').forEach(function (btn) {
      const on = btn.getAttribute('data-lang') === lang;
      btn.classList.toggle('active', on);
      btn.setAttribute('aria-pressed', String(on));
    });
  }

  async function setLang(lang) {
    if (!LANGS.includes(lang)) return;
    const dicts = await Promise.all(sources.map(async function (base) {
      const res = await fetch(base + '/' + lang + '.json');
      return res.ok ? res.json() : {};
    }));
    applyDict(Object.assign.apply(null, [{}].concat(dicts)));
    document.documentElement.lang = lang;
    localStorage.setItem(STORAGE_KEY, lang);
    markActive(lang);
  }

  function init(opts) {
    sources = (opts && (opts.sources || (opts.basePath && [opts.basePath]))) || ['.'];
    document.querySelectorAll('.lang-toggle [data-lang]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        setLang(btn.getAttribute('data-lang'));
      });
    });
    setLang(detectLang());
  }

  return { init: init, setLang: setLang };
})();
