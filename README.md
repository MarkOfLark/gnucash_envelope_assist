# gnucash_envelope_assist
Scripts that assist in using GnuCash for personal finances under the envelope system.

These scripts assume that you will have set up GnuCash with a structure similar to what is shown in the screenshot below:

![GnuCash Account Setup](gnucash_accounts.png?raw=true "GnuCash Account Setup")

The system tracks expenses by allocating all funds under the checking account into certain categories (envelopes). Each week the income is deposited into the checking account and then distributed into the envelopes and into the savings account.

# send_envelope_status.py
This script queries the given .gnucash file and then reports the balance of all sub-accounts under the given account.

email_parameters.py must be called first to set up the SMTP account that will be used to send the email.

# email_parameters.py
This script queries the user for the SMTP account information and then saves the parameters to a binary file that is used by send_envelope_status.py to connect to the SMTP server. WARNING: the account information is not stored securely.

