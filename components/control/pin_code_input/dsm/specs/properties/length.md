### Length

Defines the number of digit cells displayed in the component, typically ranging from 4 to 8 digits depending on security requirements:

- **4 digits**: Common for basic PINs and simple verification codes
- **6 digits**: Standard for most OTP and 2FA implementations (TOTP standard)
- **8 digits**: Used for high-security applications or certain authenticator systems

The length should be set based on the security requirements of your authentication system and cannot be changed during runtime.