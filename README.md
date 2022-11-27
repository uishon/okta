Okta Login
==========

Login with Okta. Return `SVPNCOOKIE`. Use in conjuction with [openconnect](https://gitlab.com/openconnect/openconnect) to connect to VPN endpoints that use Okta as their SSO provider.

Usage
-----
Install package using [pipx](https://pypa.github.io/pipx/), then
```
export SVN_HOST="https://vpn.example.com"
sudo openconnect --protocol=fortinet --cookie="SVPNCOOKIE=$(okta-login)"
```