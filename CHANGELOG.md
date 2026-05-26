# OdooIQ Intranet — Change Log

## 2026-05-26 — Webmail Link Fix

**Change:** Fixed "Open Webmail" button URL in the EMAIL section of /intranet

- **Before:** https://www2.netfirms.com/controlpanel/mail/login.html?email=john@odooiq.com
- **After:** https://emailmg.netfirms.com/roundcube/?_task=mail&_mbox=INBOX

**Location in page:** EMAIL section > Webmail (Netfirms) card > "✉ Open Webmail" button  
**Method:** Odoo Website Editor — clicked button, edited link via Link Popover, saved  
**Stored in:** ir.ui.view id=4299 (xml_id: website.intranet), arch_db field in PostgreSQL  

---

## 2026-05-26 — Mobile UX/UI Phase 1 (initial)

All CSS/JS injected via Odoo Code Injection (ir.website.custom_code_head/body).

### CSS (18 sections, ~168K chars total, all @media max-width:767px):
1. iOS BASE - tap highlights, touch-action, font-size adjust
2. HAMBURGER - 52x52px tap target  
3. HERO - padding compression
4. CALENDAR - compact rows (purple left border), organizer info hidden
5. TODO - project/date sub-line hidden
6. JUMP NAV - fixed pill bar, bottom thumb zone
7. INSTANCES CAROUSEL - horizontal swipe, PROD/DEMO badges
8. PROJECTS - Manager label hidden, compact cards
9. BUTTONS - #6d4770 filled, 48px height, full-width
10. TABLE - Backups horizontal scroll with -webkit-overflow-scrolling
11. CARDS - 14px radius, scale(0.98) press animation
12. BOTTOM NAV - 5-item fixed bar (Home, Projects, Discuss, Calendar, Apps)
13. FOOTER - cleanup
14. SAFE AREAS - env(safe-area-inset-*)
15. HERO TITLE REDUCTION - s_text_block h1 targeting
16. ONE-HANDED - FAB, swipe zones, thumb spacing, scroll snap
17. HERO DISPLAY-4 FIX - specificity override for Bootstrap display-4
18. HERO ULTRA-COMPACT - html body h1.display-4, 1.1rem, white-space nowrap

### JS (~85K chars total):
- Bottom nav bar builder (5 items, SVG icons)
- Jump nav pill bar builder (7 section shortcuts)
- Back-to-top button (left side, 76px from bottom)
- Instances carousel builder (PROD/DEMO badge detection)
- Card full-area tappability
- Pull hint div

### Page/Menu changes (Odoo DB records):
- Nav items deleted via Edit Menu: Shop, Events, Courses, Jobs, Contact us
- Phone number hidden via Show/Hide Elements toggle
- Cart icon hidden via Show/Hide Elements toggle
- Footer sections deleted: Useful Links, About us, Connect with us columns

### To extract CSS/JS from DB:
```sql
-- Connect to: psql -U odoo -d odooiq
SELECT 
  length(custom_code_head) as css_chars,
  length(custom_code_body) as js_chars
FROM ir_website WHERE id = 1;

-- Export CSS:
COPY (SELECT custom_code_head FROM ir_website WHERE id=1) TO '/tmp/mobile_ux.css.txt';

-- Export JS:
COPY (SELECT custom_code_body FROM ir_website WHERE id=1) TO '/tmp/mobile_ux.js.txt';
```

See CLAUDE_CODE_TASKS.md for full Phase 2 implementation tasks.
