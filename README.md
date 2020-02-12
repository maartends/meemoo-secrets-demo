# meemoo-secrets-demo

## Synopsis

Demo code for secrets management within meemoo.

## Warning

This is demo-code. The file which contains the secrets (`.env.secrets`) is
checked into this repository for the sole purpose of this demonstration. If you
MUST work with ANY file that contains secrets, be sure to include it into your
`.gitignore` file!

## Usage

(**Note**: be sure to use a Python3 interpreter.)

Try and execute the main file `app.py`:

    $ python app.py

No secrets are available in the environemnt nor is Vault available, thus you
get:

    KeyError: 'Key LDAP_PASSWD not available in the environment'

Make the secrets available in the environment by `source`ing the
`.env.secrets.` file;

    $ source .env.secrets

Execute the main file `app.py` again, now you should get:

    The LDAP password is: abc123

Now, make the Vault secrets backend available by modifying the file
`meemoo/vault.py`. Change:

```python
    def is_available(self):
        return False
```

to:

```python
    def is_available(self):
        return True
```

and run the code again.
