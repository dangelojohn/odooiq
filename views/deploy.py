#!/usr/bin/env python3
"""Re-deploy views/intranet.qweb.xml to the live odooiq Odoo instance.
Usage:  ODOO_URL=https://demo.odooiq.com ODOO_DB=odooiq ODOO_USER=admin ODOO_PASS=Admin!SEG ./deploy.py
"""
import os, sys, xmlrpc.client
URL  = os.environ.get("ODOO_URL",  "https://demo.odooiq.com")
DB   = os.environ.get("ODOO_DB",   "odooiq")
USER = os.environ.get("ODOO_USER", "admin")
PASS = os.environ.get("ODOO_PASS")
if not PASS:
    print("Set ODOO_PASS env var", file=sys.stderr); sys.exit(1)

with open(os.path.join(os.path.dirname(__file__), "intranet.qweb.xml")) as f:
    arch = f.read()

common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common", allow_none=True)
obj    = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object",  allow_none=True)
uid = common.authenticate(DB, USER, PASS, {})
if not uid:
    print("auth failed", file=sys.stderr); sys.exit(1)

view_ids = obj.execute_kw(DB, uid, PASS, "ir.ui.view", "search",
    [[("key","=","website.intranet")]])
if not view_ids:
    print("view 'website.intranet' not found in target DB", file=sys.stderr); sys.exit(1)

obj.execute_kw(DB, uid, PASS, "ir.ui.view", "write",
    [view_ids, {"arch_db": arch}])
print(f"redeployed arch ({len(arch)} chars) to view ids={view_ids}")
