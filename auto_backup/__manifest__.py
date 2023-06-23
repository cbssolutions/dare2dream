# modified 2023 cbssolutions.ro
# Copyright 2004-2009 Tiny SPRL (<http://tiny.be>).
# Copyright 2015 Agile Business Group <http://www.agilebg.com>
# Copyright 2016 Grupo ESOC Ingenieria de Servicios, S.L.U. - Jairo Llopis
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Database Auto-Backup",
    "summary": "Backups database; on local/sftp with username + password or key"
        "2.0.0 works also for list_db = False",
    "version": "16.0.2.0.0",
    "author": "cbssolutoins.ro"
    "Yenthe Van Ginneken, "
    "Agile Business Group, "
    "Grupo ESOC Ingenieria de Servicios, "
    "LasLabs, "
    "AdaptiveCity, "
    "Odoo Community Association (OCA),"
    "Daniel Domínguez (https://xtendoo.es)",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/server-tools",
    "category": "Tools",
    "depends": ["mail"],
    "data": [
        "data/ir_cron.xml",
        "data/mail_message_subtype.xml",
        "security/ir.model.access.csv",
        "view/db_backup_view.xml",
    ],
    "installable": True,
    "external_dependencies": {"python": ["pysftp"]},
}
