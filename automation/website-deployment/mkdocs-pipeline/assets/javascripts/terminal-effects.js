(function () {
  function ensureHeaderMeta() {
    var header = document.querySelector('.md-header');
    if (!header || document.querySelector('.tp-header-meta')) {
      return;
    }
    var meta = document.createElement('div');
    meta.className = 'tp-header-meta';
    var terminal = document.createElement('div');
    terminal.className = 'tp-header-terminal';
    var prompt = document.createElement('span');
    prompt.className = 'prompt';
    var siteKind = document.body.getAttribute('data-site-kind') || 'site';
    prompt.textContent = siteKind + '@theophysics';
    var separator = document.createElement('span');
    separator.className = 'separator';
    separator.textContent = '$';
    var command = document.createElement('span');
    command.className = 'command';
    var tagline = document.body.getAttribute('data-site-tagline') || document.title;
    command.textContent = tagline;
    terminal.appendChild(prompt);
    terminal.appendChild(separator);
    terminal.appendChild(command);
    meta.appendChild(terminal);
    header.parentNode.insertBefore(meta, header.nextSibling);
  }

  function updateClock() {
    var terminal = document.querySelector('.tp-header-terminal');
    if (!terminal) return;
    var existing = terminal.querySelector('.timestamp');
    if (!existing) {
      existing = document.createElement('span');
      existing.className = 'timestamp';
      existing.style.marginLeft = '0.6rem';
      existing.style.color = 'var(--tp-muted)';
      terminal.appendChild(existing);
    }
    var now = new Date();
    existing.textContent = now.toISOString().slice(0, 19).replace('T', ' ');
  }

  document.addEventListener('DOMContentLoaded', function () {
    ensureHeaderMeta();
    updateClock();
    setInterval(updateClock, 1000 * 30);
  });
})();
