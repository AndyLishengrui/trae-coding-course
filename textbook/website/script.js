/* ============================================================
   剑道试炼 Website JavaScript
   Dark mode, search, navigation, code copy
   ============================================================ */

(function () {
    'use strict';

    /* ---------- Dark Mode Toggle ---------- */
    function initDarkMode() {
        var toggle = document.querySelector('.dark-toggle');
        if (!toggle) return;

        // Load saved preference
        var saved = localStorage.getItem('jd-theme');
        if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.setAttribute('data-theme', 'dark');
            toggle.textContent = '☀';
        }

        toggle.addEventListener('click', function () {
            var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            if (isDark) {
                document.documentElement.removeAttribute('data-theme');
                toggle.textContent = '☾';
                localStorage.setItem('jd-theme', 'light');
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                toggle.textContent = '☀';
                localStorage.setItem('jd-theme', 'dark');
            }
        });
    }

    /* ---------- Mobile Menu Toggle ---------- */
    function initMobileMenu() {
        var btn = document.querySelector('.menu-toggle');
        var links = document.querySelector('.nav-links');
        if (!btn || !links) return;

        btn.addEventListener('click', function () {
            links.classList.toggle('open');
        });

        // Close on link click
        links.addEventListener('click', function (e) {
            if (e.target.tagName === 'A') {
                links.classList.remove('open');
            }
        });
    }

    /* ---------- Scroll-to-Top Button ---------- */
    function initScrollTop() {
        var btn = document.querySelector('.scroll-top');
        if (!btn) return;

        window.addEventListener('scroll', function () {
            if (window.scrollY > 300) {
                btn.classList.add('visible');
            } else {
                btn.classList.remove('visible');
            }
        });

        btn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    /* ---------- Code Reference: Search & Filter ---------- */
    function initCodeSearch() {
        var searchInput = document.getElementById('code-search');
        var chapterFilter = document.getElementById('chapter-filter');
        var entries = document.querySelectorAll('.code-entry');
        var resultCount = document.getElementById('result-count');
        if (!searchInput || !entries.length) return;

        function filterEntries() {
            var query = searchInput.value.toLowerCase().trim();
            var chapter = chapterFilter ? chapterFilter.value : 'all';
            var visible = 0;

            entries.forEach(function (entry) {
                var text = entry.textContent.toLowerCase();
                var entryChapter = entry.getAttribute('data-chapter') || '';
                var matchQuery = !query || text.indexOf(query) !== -1;
                var matchChapter = chapter === 'all' || entryChapter === chapter;

                if (matchQuery && matchChapter) {
                    entry.style.display = '';
                    visible++;
                } else {
                    entry.style.display = 'none';
                }
            });

            if (resultCount) {
                resultCount.textContent = visible + ' / ' + entries.length + ' 题';
            }
        }

        searchInput.addEventListener('input', filterEntries);
        if (chapterFilter) {
            chapterFilter.addEventListener('change', filterEntries);
        }
    }

    /* ---------- Code Reference: Expand/Collapse ---------- */
    function initCodeToggle() {
        document.addEventListener('click', function (e) {
            var header = e.target.closest('.code-entry-header');
            if (!header) return;

            var entry = header.closest('.code-entry');
            if (!entry) return;

            entry.classList.toggle('expanded');
        });
    }

    /* ---------- Copy Code Button ---------- */
    function initCopyButtons() {
        document.addEventListener('click', function (e) {
            var btn = e.target.closest('.copy-btn');
            if (!btn) return;

            var codeBlock = btn.nextElementSibling;
            if (!codeBlock) {
                codeBlock = btn.parentElement.querySelector('pre code');
            }
            if (!codeBlock) return;

            // Get plain text (strip HTML tags)
            var text = codeBlock.textContent || codeBlock.innerText;

            if (navigator.clipboard) {
                navigator.clipboard.writeText(text).then(function () {
                    showCopied(btn);
                });
            } else {
                // Fallback
                var textarea = document.createElement('textarea');
                textarea.value = text;
                textarea.style.position = 'fixed';
                textarea.style.opacity = '0';
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);
                showCopied(btn);
            }
        });

        function showCopied(btn) {
            var original = btn.textContent;
            btn.textContent = '✓ 已复制';
            btn.classList.add('copied');
            setTimeout(function () {
                btn.textContent = original;
                btn.classList.remove('copied');
            }, 2000);
        }
    }

    /* ---------- Language Tabs ---------- */
    function initLangTabs() {
        document.addEventListener('click', function (e) {
            var tab = e.target.closest('.lang-tab');
            if (!tab) return;

            var container = tab.closest('.lang-tabs');
            if (!container) return;

            // Deactivate all tabs
            container.querySelectorAll('.lang-tab').forEach(function (t) {
                t.classList.remove('active');
            });
            tab.classList.add('active');

            // Show corresponding code block
            var lang = tab.getAttribute('data-lang');
            var parent = container.parentElement;
            parent.querySelectorAll('.lang-code').forEach(function (block) {
                if (block.getAttribute('data-lang') === lang) {
                    block.style.display = '';
                } else {
                    block.style.display = 'none';
                }
            });
        });
    }

    /* ---------- Active Sidebar Link ---------- */
    function initSidebarHighlight() {
        var links = document.querySelectorAll('.chapter-sidebar .chapter-list a');
        if (!links.length) return;

        var currentFile = window.location.pathname.split('/').pop();
        links.forEach(function (link) {
            if (link.getAttribute('href') === currentFile) {
                link.classList.add('active');
            }
        });
    }

    /* ---------- Initialize ---------- */
    document.addEventListener('DOMContentLoaded', function () {
        initDarkMode();
        initMobileMenu();
        initScrollTop();
        initCodeSearch();
        initCodeToggle();
        initCopyButtons();
        initLangTabs();
        initSidebarHighlight();
    });

})();
