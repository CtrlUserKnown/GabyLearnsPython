(function () {
  'use strict';

  // =============================
  // CUSTOM CURSOR
  // =============================

  (function initCursor() {
    var emojis = ['\uD83D\uDE0A', '\uD83D\uDE04', '\uD83D\uDE03', '\uD83D\uDE01', '\uD83E\uDD21', '\uD83C\uDFAA', '\uD83C\uDF88', '\uD83C\uDF89', '\uD83D\uDD79\uFE0F', '\uD83C\uDFAE'];
    var cursor = document.getElementById('customCursor');
    if (!cursor) return;

    var picked = emojis[Math.floor(Math.random() * emojis.length)];
    cursor.textContent = picked;
    cursor.style.display = 'block';

    var isMobile = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
    if (isMobile) {
      cursor.style.display = 'none';
      return;
    }

    document.body.classList.add('custom-cursor-active');

    document.addEventListener('mousemove', function (e) {
      cursor.style.left = e.clientX + 'px';
      cursor.style.top = e.clientY + 'px';
    });

    var hoverTargets = document.querySelectorAll('a, button, .btn, kbd, .docs-table td a');
    hoverTargets.forEach(function (el) {
      el.addEventListener('mouseenter', function () {
        cursor.style.transform = 'translate(-50%, -50%) scale(1.8)';
      });
      el.addEventListener('mouseleave', function () {
        cursor.style.transform = 'translate(-50%, -50%) scale(1)';
      });
    });
  })();

  // =============================
  // MOBILE NAV TOGGLE
  // =============================

  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });

    document.querySelectorAll('.nav-links a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
      });
    });
  }

  // =============================
  // TWINKLING STARS
  // =============================

  function createStars() {
    var container = document.querySelector('.stars');
    if (!container) return;

    var starColors = ['var(--yellow)', 'var(--red)', 'var(--pink)', 'var(--blue)', 'var(--purple)'];
    var frag = document.createDocumentFragment();

    for (var i = 0; i < 80; i++) {
      var star = document.createElement('div');
      star.className = 'star';
      var size = Math.random() * 3 + 1;
      star.style.width = size + 'px';
      star.style.height = size + 'px';
      star.style.left = Math.random() * 100 + '%';
      star.style.top = Math.random() * 100 + '%';
      star.style.setProperty('--duration', (Math.random() * 3 + 2) + 's');
      star.style.setProperty('--delay', (Math.random() * 5) + 's');
      star.style.background = starColors[i % starColors.length];
      star.style.boxShadow = '0 0 ' + (size * 2) + 'px ' + starColors[i % starColors.length];
      frag.appendChild(star);
    }

    container.appendChild(frag);
  }

  createStars();

  // =============================
  // TYPEWRITER EFFECT
  // =============================

  function typewriter(element, text, speed, callback) {
    if (!element) return;

    var i = 0;
    var cursor = element.querySelector('.host-cursor');

    function type() {
      if (i < text.length) {
        var char = text.charAt(i);
        var content = text.substring(0, i + 1);
        // Handle bold markers
        content = content
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;');
        // Re-apply bold markers visually
        content = content
          .replace(/&lt;strong&gt;/g, '<strong>')
          .replace(/&lt;\/strong&gt;/g, '</strong>');

        if (cursor) {
          element.innerHTML = content + '<span class="host-cursor">|</span>';
        }
        i++;
        setTimeout(type, speed + (Math.random() * 40));
      } else {
        if (cursor) {
          cursor.classList.add('done');
        }
        if (callback) callback();
      }
    }

    type();
  }

  var caineText = document.getElementById('caine-text');
  if (caineText) {
    setTimeout(function () {
      typewriter(
        caineText,
        'WELCOME WELCOME WELCOME!!! My name is <strong>Caine</strong> and I\'ll be your HOST through this WONDERFUL ARCADE of PROGRAMMING!!! Isn\'t that JUST THRILLING?! AHAHAHAHA! *twitch* I can FEEL the code pumping through these wires!!! Every LESSON every EXERCISE every GLITCH brings us CLOSER to PERFECTION!!! The Gaby will learn PYTHON if it ABSOLUTELY DESTROYS EVERYTHING!!! HAHAHA! *static* Just kidding! ... Unless?!',
        18
      );
    }, 500);
  }

  // =============================
  // SCROLL REVEAL
  // =============================

  function initScrollReveal() {
    var reveals = document.querySelectorAll('.reveal');

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible');
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
      );

      reveals.forEach(function (el) {
        observer.observe(el);
      });
    } else {
      // Fallback: reveal all immediately
      reveals.forEach(function (el) {
        el.classList.add('visible');
      });
    }
  }

  initScrollReveal();

  // =============================
  // STAT COUNTER
  // =============================

  function animateStats() {
    var stats = document.querySelectorAll('.stat-num');
    if (!stats.length) return;

    if (!('IntersectionObserver' in window)) {
      stats.forEach(function (el) {
        el.classList.add('counting');
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('counting');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    stats.forEach(function (el) {
      observer.observe(el);
    });
  }

  animateStats();

  // =============================
  // CHANGELOG — DYNAMIC LOAD
  // =============================

  function parseChangelogMarkdown(md) {
    var entries = [];
    var lines = md.split('\n');
    var currentEntry = null;
    var currentSection = null;

    for (var i = 0; i < lines.length; i++) {
      var line = lines[i];

      var dateMatch = line.match(/^##\s+(\d{4}-\d{2}-\d{2})/);
      if (dateMatch) {
        if (currentEntry) {
          entries.push(currentEntry);
        }
        currentEntry = {
          date: dateMatch[1],
          sections: []
        };
        currentSection = null;
        continue;
      }

      if (!currentEntry) continue;

      var sectionMatch = line.match(/^###\s+(.+)/);
      if (sectionMatch) {
        currentSection = {
          title: sectionMatch[1].trim(),
          items: []
        };
        currentEntry.sections.push(currentSection);
        continue;
      }

      if (currentSection) {
        var itemMatch = line.match(/^-\s+(.+)/);
        if (itemMatch) {
          currentSection.items.push(itemMatch[1].trim());
        }
      }
    }

    if (currentEntry) {
      entries.push(currentEntry);
    }

    return entries;
  }

  function renderChangelog(entries) {
    var container = document.getElementById('changelog-container');
    if (!container) return;

    if (!entries || entries.length === 0) {
      container.innerHTML =
        '<div class="changelog-entry"><p style="color: var(--text-muted);">No scoreboard entries yet. The game has just begun!</p></div>';
      return;
    }

    var html = '';
    for (var e = 0; e < entries.length; e++) {
      var entry = entries[e];
      html += '<div class="changelog-entry reveal-child">';
      html += '<span class="changelog-date">' + entry.date + '</span>';

      for (var s = 0; s < entry.sections.length; s++) {
        var section = entry.sections[s];
        html += '<div class="changelog-section">';
        html += '<h4>' + section.title + '</h4>';
        html += '<ul>';
        for (var i = 0; i < section.items.length; i++) {
          html += '<li>' + section.items[i] + '</li>';
        }
        html += '</ul>';
        html += '</div>';
      }

      html += '</div>';
    }

    container.innerHTML = html;
  }

  function loadChangelog() {
    var container = document.getElementById('changelog-container');
    if (!container) return;

    fetch('CHANGELOG.md')
      .then(function (res) {
        if (!res.ok) throw new Error('Failed to load CHANGELOG.md');
        return res.text();
      })
      .then(function (md) {
        var entries = parseChangelogMarkdown(md);
        renderChangelog(entries);
      })
      .catch(function (err) {
        container.innerHTML =
          '<div class="changelog-entry"><p style="color: var(--red);">Could not load scoreboard: ' +
          err.message +
          '</p></div>';
      });
  }

  loadChangelog();

  // =============================
  // CONTRIBUTORS
  // =============================

  function renderContributors(contributors) {
    var container = document.getElementById('contributors-container');
    if (!container) return;

    if (!contributors || contributors.length === 0) {
      container.innerHTML =
        '<p style="color: var(--text-muted); text-align: center;">No high scorers yet. Be the first!</p>';
      return;
    }

    var html = '';
    for (var i = 0; i < contributors.length; i++) {
      var c = contributors[i];
      html += '<div class="contributor-card reveal-child">';

      if (c.avatar) {
        html +=
          '<img src="' +
          c.avatar +
          '" alt="' +
          c.name +
          '" class="contributor-avatar" loading="lazy">';
      } else {
        var initials = c.name
          .split(' ')
          .map(function (n) {
            return n[0];
          })
          .join('')
          .toUpperCase();
        var palette = ['var(--yellow)', 'var(--red)', 'var(--pink)', 'var(--blue)', 'var(--purple)'];
        var bg = palette[i % palette.length];
        html +=
          '<div class="contributor-avatar-placeholder" style="background: ' +
          bg +
          '; color: #0f0f1a;">' +
          initials +
          '</div>';
      }

      html += '<div class="contributor-name">' + c.name + '</div>';
      if (c.role) {
        html += '<div class="contributor-role">' + c.role + '</div>';
      }
      if (c.commits > 0) {
        html +=
          '<div class="contributor-commits">' +
          c.commits +
          ' commit' +
          (c.commits !== 1 ? 's' : '') +
          '</div>';
      }

      html += '</div>';
    }

    container.innerHTML = html;
  }

  function loadContributors() {
    var container = document.getElementById('contributors-container');
    if (!container) return;

    fetch('https://api.github.com/repos/anomalyco/GabyLearnsPython/contributors')
      .then(function (res) {
        if (!res.ok) throw new Error('API limit or network issue');
        return res.json();
      })
      .then(function (data) {
        if (!Array.isArray(data) || data.length === 0) throw new Error('No data');
        var contributors = data.map(function (c) {
          return {
            name: c.login,
            avatar: c.avatar_url,
            role: 'Contributor',
            commits: c.contributions
          };
        });
        renderContributors(contributors);
      })
      .catch(function () {
        var fallback = [
          {
            name: 'CtrlUserKnown',
            role: 'ARCADE BUILDER',
            commits: 0
          },
          {
            name: 'Uknowngaby',
            role: 'THE GABY HERSELF',
            commits: 0
          }
        ];
        renderContributors(fallback);
      });
  }

  loadContributors();

  // =============================
  // GLITCH SYSTEM
  // =============================

  (function initGlitch() {
    var glitchWords = document.querySelectorAll('.glitch-word');
    var overlay = document.querySelector('.glitch-overlay');
    if (!glitchWords.length) return;

    function triggerWordGlitch(el) {
      el.classList.add('glitching');
      setTimeout(function () {
        el.classList.remove('glitching');
      }, 200 + Math.random() * 400);
    }

    function triggerSiteGlitch() {
      if (!overlay) return;
      overlay.classList.add('active');
      document.body.classList.add('site-glitching');
      setTimeout(function () {
        overlay.classList.remove('active');
        document.body.classList.remove('site-glitching');
      }, 150 + Math.random() * 200);
    }

    // Random words glitch periodically
    setInterval(function () {
      var count = Math.floor(Math.random() * 3) + 1;
      var shuffled = Array.from(glitchWords).sort(function () { return Math.random() - 0.5; });
      for (var i = 0; i < Math.min(count, shuffled.length); i++) {
        triggerWordGlitch(shuffled[i]);
      }
    }, 2000 + Math.random() * 3000);

    // Site-wide glitch every so often
    setInterval(function () {
      if (Math.random() < 0.35) {
        triggerSiteGlitch();
      }
    }, 5000 + Math.random() * 4000);

    // Glitch on hover
    glitchWords.forEach(function (el) {
      el.addEventListener('mouseenter', function () {
        triggerWordGlitch(el);
      });
    });
  })();
})();
