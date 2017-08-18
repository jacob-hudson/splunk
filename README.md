# splunk

## Vanilla install
- Clone the repo
- Start the VM with `vagrant up`
- Enter the VM with `vagrant ssh`
- Go to `/vagrant`
- Start the setup with `chmod +x && ./install.sh`
- After accepting the license, the Splunk instance will be available at the following:
  - `https://127.0.0.1:8000`
  - `admin/changeme`

## Getting files from the VM (using `scp`)
- `scp -i _IdentityFile_ -P _Port_  _Src_ _Dest_ `
  - The location of _IdentityFile_ and _Port_ can be extrated from `vagrant ssh-config`
