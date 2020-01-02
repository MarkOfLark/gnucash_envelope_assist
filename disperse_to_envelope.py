import datetime
import argparse


def main():
    parser = argparse.ArgumentParser(description='Disperse to accounts')
    parser.add_argument('-t','--transaction-list',required=True,
                        help='TOML file describing transactions for the dispersement')
    parser.add_argument('-r','--root-account', required=True,
                        help='Root account string exactly as displayed in GnuCash')
    parser.add_argument('-l','--left-over-account', required=True,
                        help='Account string exactly as displayed in GnuCash which accepts any left-over funds after dispersment.')
    parser.add_argument('-g','--gnucash-ledger', required=True,
                        help='GnuCash file to use for this dispersement')

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    # execute only if run as a script
    main()