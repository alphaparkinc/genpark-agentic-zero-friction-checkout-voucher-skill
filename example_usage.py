from client import AgenticZeroFrictionCheckoutVoucherClient

def main():
    client = AgenticZeroFrictionCheckoutVoucherClient()
    res = client.mint_checkout_voucher('did:key:z6Mkn882190', 299.00)
    print('Zero-Friction Checkout Voucher: ' + res['checkout_voucher_id'])
    print('Passkey Verified: ' + str(res['delegated_passkey_verified']) + ' | Zero-Click: ' + str(res['zero_click_checkout_authorized']))
    print('Expires: ' + res['voucher_expiration_iso'])
    print('Handoff Payload: ' + res['merchant_settlement_handoff_payload_url'])

if __name__ == '__main__':
    main()
