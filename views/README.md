# OdooIQ Intranet — view customizations

The intranet page at `https://www.odooiq.local:9448/intranet` (or `/`) is a customized website page in the odooiq Odoo instance. This directory captures its design so it can be redeployed if the DB is rebuilt.

## Files

| File | Purpose |
|---|---|
| `intranet.qweb.xml` | The raw QWeb template arch — the content you see in Odoo's website editor under view key `website.intranet` |
| `intranet.deployable.xml` | Odoo-module-style XML wrapper (for `__manifest__.py` data files) — empty arch, see README |
| `deploy.py` | Reads `intranet.qweb.xml` and re-applies it to the live instance via XML-RPC |

## Sections rendered by this template

1. Header — "OdooIQ Intranet"
2. **Today's Calendar — John** (dynamic; queries `calendar.event` for partner=john today)
3. **To Do — John** (dynamic; queries `project.task` for user_ids includes john)
4. **Email** (static button → Netfirms webmail for john@odooiq.com)
5. Odoo Instances — 8 cards (OdooIQ + AlfaCore + 7 demos)
6. Projects — dynamic list from `project.project`
7. Backups — reads `ir.config_parameter` key `odooiq.backups_section_html`
8. **Developer Tools** — 9 cards (CGI, Forgejo LAN+org, QNAP LAN+Public, Cloudflare main+ZT, Odoo source, OCA)

## Redeploying

If the odooiq DB is rebuilt from scratch:

```bash
ODOO_PASS=YourPassword ./deploy.py
```

The view (key `website.intranet`) is created by the website-page setup; this script only updates its `arch_db`. If the page itself doesn't exist, create it via Odoo's website builder first (Website → Site → Pages → New, URL `/intranet`).

Snapshot date: 2026-05-26.
