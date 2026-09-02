class AgenticZeroFrictionCheckoutVoucherClient:
    def mint_checkout_voucher(self, buyer_verified_identity='did:key:z6Mku...9182', order_total_usd=149.99, shipping_address_hash='sha256_7a9f8c12b4e8'):
        return {
            'checkout_voucher_id': 'vch_chk_8812',
            'delegated_passkey_verified': True,
            'voucher_expiration_iso': '2026-09-02T16:30:00Z',
            'zero_click_checkout_authorized': True,
            'merchant_settlement_handoff_payload_url': 'https://voucher.commerce.genpark.ai/handoffs/8812.json'
        }
