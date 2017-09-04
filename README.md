# splunk

## Vanilla install
- Clone the repo
- Start the VM with `vagrant up`
- Enter the VM with `vagrant ssh`
- Go to `/vagrant`
- Start the setup with `chmod +x && ./install_rpm.sh` or `chmod +x && ./install_tgz.sh`, depending on your preferences/requirements
- After accepting the license, the Splunk instance will be available at the following:
  - `https://127.0.0.1:8000`
  - `admin/changeme`

## Getting files from the VM (using `scp`)
- `scp -i _IdentityFile_ -P _Port_  _Src_ _Dest_ `
  - The location of _IdentityFile_ and _Port_ can be extrated from `vagrant ssh-config`

## Incorrect timezone?
- Use `date` to check the time
- Adjust timezone with `timedatectl set-timezone America/Chicago` replacing `America/Chicago` with the correct timezone
- The root password (needed for `timedatectl`) is `vagrant`
