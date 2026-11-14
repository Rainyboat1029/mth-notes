(function () {
  "use strict";
  var lastUrl = "";

  function render() {
    if (!window.renderMathInElement) return;
    if (location.href === lastUrl) return;
    lastUrl = location.href;
    var root = document.querySelector(".md-content__inner") || document.querySelector(".md-content") || document.body;
    window.renderMathInElement(root, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "\\[", right: "\\]", display: true },
        { left: "$", right: "$", display: false },
        { left: "\\(", right: "\\)", display: false }
      ],
      throwOnError: false,
      strict: false,
      ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "option"]
    });
  }

  document.addEventListener("DOMContentLoaded", render);
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(render);
  }
  render();
})();
