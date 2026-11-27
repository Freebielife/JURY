"""JURY-specific identity and unavailable-market regressions."""
import base64
import binascii
import json
import unittest
from pathlib import Path
from scripts.project_runtime import canonical_address, check_identity
import trades

ROOT = Path(__file__).resolve().parents[1]

class JuryIdentityTests(unittest.TestCase):
    def test_masterchain_round_trip_and_basechain_are_distinct(self):
        cfg=json.loads((ROOT/'project.json').read_text())
        raw='-1:bf7e01ea11ccc2b302e99c112822f832aee254be7fd00ede5046379c63cc3796'
        self.assertEqual(canonical_address(cfg['master']),raw)
        body=bytes([0x11,0])+bytes.fromhex(raw.split(':')[1])
        base=base64.urlsafe_b64encode(body+binascii.crc_hqx(body,0).to_bytes(2,'big')).decode()
        self.assertNotEqual(canonical_address(base),raw)
        with self.assertRaises(ValueError):
            check_identity({'schema':1,'token':base},cfg)

    def test_no_unverified_pool_or_price_source(self):
        cfg=json.loads((ROOT/'project.json').read_text())
        self.assertEqual(cfg['pools'],[])
        self.assertIsNone(cfg['primary_pool'])
        self.assertEqual(trades.POOLS,{})
        self.assertIsNone(trades.PRIMARY)

    def test_supplied_artwork_and_no_invented_channel(self):
        cfg=json.loads((ROOT/'project.json').read_text())
        self.assertEqual((ROOT/'web/project-logo.webp').read_bytes(),(ROOT/'web/project-flag.webp').read_bytes())
        self.assertNotIn('telegram',cfg['links'])

    def test_layout_keeps_extra_notices_and_empty_supply_out_of_view(self):
        page=(ROOT/'web/page.html').read_text()
        self.assertNotIn('coverageNotice',page)
        self.assertIn('class="panel resources supplyPanel" hidden',page)
        self.assertIn('href="#supply" data-t="navSupply" hidden',page)
        self.assertIn('href="https://telemarket.org/oracle/dao"',page)
        self.assertIn('href="https://dyor.io/token/Ef-_fgHqEczCswLpnBEoIvgyruJUvn_QDt5QRjecY8w3lr2i"',page)
