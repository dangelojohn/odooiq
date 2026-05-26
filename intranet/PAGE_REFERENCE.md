# OdooIQ Intranet Page Reference

## Page Details
- URL: /intranet
- Odoo View XML ID: website.intranet
- ir.ui.view id: 4299
- ir.website id: 1

## Page Sections (in order)
1. Hero — "OdooIQ Intranet" title, "Central hub for every service..." description
2. Jump Navigation — pill bar: Calendar | To Do | Email | Instances | Projects | Backups | Dev
3. CALENDAR section — Today's Calendar (John), compact list view, "Open Calendar app →"
4. TO DO section — John's tasks, compact list view, "Open Projects app →"
5. EMAIL section — Webmail (Netfirms) card
6. ODOO INSTANCES section — carousel: OdooIQ (PROD), AlfaCore (PROD), Southbrook (DEMO)...
7. PROJECTS section — AlfaCore, Southbrook Cabinetry, Tribancs cards
8. BACKUPS section — table with all instances backup status
9. DEVELOPER TOOLS section — OdooIQ Server CGI, Forgejo LAN, Forgejo qnap.org, QNAP Admin cards
10. Footer — copyright only

## Key Links (as of 2026-05-26)

### EMAIL Section
- Button: "✉ Open Webmail"
- URL: https://emailmg.netfirms.com/roundcube/?_task=mail&_mbox=INBOX
- Note: Fixed 2026-05-26 (was: www2.netfirms.com/controlpanel/mail/login.html?email=john@odooiq.com)

### ODOO INSTANCES
- OdooIQ (PROD): https://odoo.odooiq.com (or internal URL)
- AlfaCore (PROD): https://odoo.alfacore.ca
- Other instances: Southbrook, Tribancs, Porterly, Sapienzium, OdooAI

### DEVELOPER TOOLS
- Forgejo (LAN): https://192.168.68.108:9443/git/
- Forgejo (qnap.org): https://git.qnap.org/qnap/
- QNAP Admin LAN: https://192.168.68.108:8080/
- Cloudflare Dashboard: https://dash.cloudflare.com/
- Cloudflare Zero Trust: https://one.dash.cloudflare.com/

## Header
- Navbar: Home only (Shop, Events, Courses, Jobs, Contact us deleted)
- Phone: hidden via Show/Hide Elements
- Cart: hidden via Show/Hide Elements
- Contact CTA button: present in template (needs XML override in theme module)

## To Export Page HTML from DB
```sql
-- Get the page view arch (the actual HTML content)
SELECT arch_db FROM ir_ui_view WHERE xml_id = 'website.intranet';
-- OR
SELECT arch_db FROM ir_ui_view WHERE id = 4299;
```

## CSS/JS (Code Injection)
- Location: ir.website id=1, fields: custom_code_head, custom_code_body
- CSS: ~168K chars (18 mobile-only sections, @media max-width:767px)
- JS: ~85K chars (bottom nav, jump nav, carousel, back-to-top, card tappability)
- See CLAUDE_CODE_TASKS.md for migration instructions
