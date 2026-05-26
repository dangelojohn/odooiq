# Claude Code Tasks — OdooIQ Intranet Mobile UX/UI

## Project Context

**Server:** www.odooiq.local:9448 | Odoo 19 EE  
**Git Repo:** https://192.168.68.108:9443/git/qnap/odooiq (main branch)  
**Auth User:** John (john@odooiq.com), admin  
**Page:** /intranet — OdooIQ Intranet homepage  
**Status:** Phase 1 COMPLETE (Odoo Code Injection DB) -> Phase 2 needed (Git module)

---

## What Was Done (Phase 1)

CSS/JS injected into Odoo DB via Website Editor -> Theme -> Code Injection.

### CSS Sections (18 total, all @media max-width:767px):
1. iOS BASE - tap highlights, touch-action, font-size adjust
2. HAMBURGER - 52x52px tap target
3. HERO - padding compression
4. CALENDAR - compact rows (purple border), organizer info hidden
5. TODO - sub-line (project/date) hidden
6. JUMP NAV - fixed pill bar bottom thumb zone
7. INSTANCES CAROUSEL - horizontal swipe, PROD/DEMO badges
8. PROJECTS - Manager label hidden, compact cards
9. BUTTONS - #6d4770 filled, 48px height, full-width
10. TABLE - Backups horizontal scroll with -webkit-overflow-scrolling
11. CARDS - 14px radius, scale(0.98) press animation
12. BOTTOM NAV - 5-item fixed (Home, Projects, Discuss, Calendar, Apps)
13. FOOTER - cleanup
14. SAFE AREAS - env(safe-area-inset-*)
15. HERO TITLE REDUCTION - s_text_block h1 targeting
16. ONE-HANDED - FAB, swipe zones, thumb spacing
17. HERO DISPLAY-4 FIX - specificity override
18. HERO ULTRA-COMPACT - html body h1.display-4, 1.1rem, nowrap

### JS Features:
- Bottom nav builder (5 items, SVG icons)
- Jump nav builder (7 sections)
- Back-to-top button (left side for right-thumb users)
- Instances carousel builder
- Card tappability

### DB Changes (non-code):
- Nav items deleted: Shop, Events, Courses, Jobs, Contact us
- Phone + Cart hidden via Show/Hide Elements
- Footer sections deleted: Useful Links, About us, Connect with us

---

## TASK 1 - Create Odoo Module

Path: /opt/odoo/addons/theme_odooiq_intranet/

Module structure:
- __init__.py (empty)
- __manifest__.py
- static/src/scss/mobile_ux.scss (CSS from DB)
- static/src/js/mobile_ux.js (JS from DB)
- views/website_templates.xml (header overrides)

__manifest__.py:

    {
        'name': 'OdooIQ Intranet Mobile UX',
        'version': '19.0.1.0.0',
        'category': 'Website/Theme',
        'depends': ['website'],
        'data': ['views/website_templates.xml'],
        'assets': {
            'web.assets_frontend': [
                'theme_odooiq_intranet/static/src/scss/mobile_ux.scss',
                'theme_odooiq_intranet/static/src/js/mobile_ux.js',
            ],
        },
        'installable': True,
        'license': 'LGPL-3',
    }

---

## TASK 2 - Export CSS/JS from Odoo DB

SQL:

    SELECT custom_code_head, custom_code_body FROM ir_website WHERE id = 1;

- Strip outer <style>...</style> tags from custom_code_head -> mobile_ux.scss
- Strip outer <script>...</script> tags from custom_code_body -> mobile_ux.js

Clear DB after migration via Odoo shell:

    odoo shell -d odooiq --no-http
    website = env['ir.website'].browse(1)
    website.write({'custom_code_head': '', 'custom_code_body': ''})
    env.cr.commit()

---

## TASK 3 - XML Header Override

views/website_templates.xml:

    <?xml version="1.0" encoding="utf-8"?>
    <odoo>
      <template id="website.template_header_no_cta"
                inherit_id="website.template_header_default"
                name="OdooIQ - Remove Contact CTA">
        <xpath expr="//t[@t-call='website.placeholder_header_call_to_action']"
               position="replace"/>
      </template>
    </odoo>

---

## TASK 4 - Install and Verify

1. Restart: docker-compose restart odoo
2. Install: /odoo/settings -> Apps -> OdooIQ Intranet Mobile UX -> Install
3. Verify at 390px viewport:
   - getComputedStyle(h1).fontSize == "17.6px" (1.1rem)
   - document.getElementById('iq-bottom-nav') != null
   - document.getElementById('iq-jump-nav') != null
   - ir_website.custom_code_head == ''

---

## TASK 5 - Commit and Push

    git add theme_odooiq_intranet/
    git commit -m "feat: Add theme_odooiq_intranet mobile UX module

    - iPhone-optimized CSS (18 sections, @media max-width:767px)
    - Bottom nav bar (5 items: Home, Projects, Discuss, Calendar, Apps)
    - Jump nav pill bar (7 section shortcuts)
    - Back-to-top button (left side for right-thumb operation)
    - Hero compression: h1 display-4 -> 1.1rem single line
    - Calendar compact: purple border, organizer info hidden
    - Todo compact: sub-line hidden
    - One-handed UX: scroll snap, thumb zones, FAB
    - Safe area insets for iPhone notch/home indicator
    - Migrated from Odoo Code Injection to versioned module"

    git push origin main

---

## TASK 6 - Future Enhancements (Optional)

1. PWA Manifest + Add to Home Screen icon
2. Dark mode (@media prefers-color-scheme: dark)
3. Notification badges on bottom nav items
4. Collapsible accordion section cards
5. Left/right swipe between sections
6. Service Worker offline cache for /intranet

---

## Key CSS Selectors

| Element | Selector |
|---------|----------|
| Hero h1 | h1.display-4.fw-bold.mb-2 |
| Hero description | p.lead.text-muted.mb-0 |
| Hero section | .s_text_block.pt-5.o_colored_level |
| Calendar events | .list-group-item |
| Organizer info | .flex-grow-1 .small.text-muted |
| Todo items | .list-group-item |
| Project manager | .card-body > p.small.text-muted |
| Bottom nav | #iq-bottom-nav |
| Jump nav | #iq-jump-nav |
| Back-to-top | #iq-back-top |

## Design Tokens

| Token | Value |
|-------|-------|
| Primary purple | #6d4770 |
| Min tap height | 48px |
| Hamburger size | 52x52px |
| Mobile breakpoint | max-width 767px |
| Card border-radius | 14px |
| Pill border-radius | 24px |
| Bottom nav height | 60px + env(safe-area-inset-bottom) |
| Hero h1 size | 1.1rem (17.6px) |
| Hero description | 0.7rem |

---

*Created: 2026-05-26 by Claude (Browser Automation) | Status: Ready for Claude Code implementation*