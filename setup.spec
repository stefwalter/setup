Summary: A set of system configuration and setup files.
Name: setup
Version: 2.3.4
Release: 1
Copyright: public domain
Group: System Environment/Base
Source: setup-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-root
BuildArchitectures: noarch
Conflicts: initscripts < 4.26

%description
The setup package contains a set of important system configuration and
setup files, such as passwd, group, and profile.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cp -ar * $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/var/log
cp /dev/null $RPM_BUILD_ROOT/var/log/lastlog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%verify(not md5 size mtime) %config(noreplace) /etc/passwd
%verify(not md5 size mtime) %config(noreplace) /etc/group
%verify(not md5 size mtime) %config /etc/services
%verify(not md5 size mtime) %config(noreplace) /etc/exports
%config(noreplace) /etc/filesystems
%config(noreplace) /etc/host.conf
%verify(not md5 size mtime) %config(noreplace) /etc/hosts.allow
%verify(not md5 size mtime) %config(noreplace) /etc/hosts.deny
%verify(not md5 size mtime) %config /etc/motd
%config(noreplace) /etc/printcap
%config /etc/inputrc
%config(noreplace) /etc/profile
%config /etc/protocols
%attr(0600,root,root) %config(missingok) /etc/securetty
%config(noreplace) /etc/csh.login
%config(noreplace) /etc/csh.cshrc
%dir /etc/profile.d
%config(noreplace) %verify(not md5 size mtime) /var/log/lastlog

%changelog
* Sun Aug  6 2000 Bill Nottingham <notting@redhat.com>
- /var/log/lastlog is %config(noreplace) (#15412)
- some of the various %verify changes (#14819)

* Thu Aug  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- linuxconf should be 98, not 99

* Tue Jul 25 2000 Bill Nottingham <notting@redhat.com>
- fix some of the csh stuff (#14622)

* Sun Jul 23 2000 Nalin Dahyabhai <nalin@redhat.com>
- stop setting "multi on" in /etc/host.conf

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 27 2000 Bill Nottingham <notting@redhat.com>
- add hfs filesystem

* Wed Jun 21 2000 Preston Brown <pbrown@redhat.com>
- printcap is a noreplace file now

* Sun Jun 18 2000 Bill Nottingham <notting@redhat.com>
- fix typo

* Tue Jun 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- add linuxconf/tcp = 99 to /etc/services

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- add some stuff to /etc/services
- tweak ulimit call again

* Tue Jun  6 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- homedir of ftp is now /var/ftp

* Sun May 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- move profile.d logic in csh.login to csh.cshrc

* Tue Apr 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- redirect ulimit -S -c to /dev/null to avoid clutter

* Thu Apr 13 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- s/ulimit -c/ulimit -S -c/ - bash 2.x adaption

* Mon Apr 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- Add more of the kerberos-related services from IANA's registry and krb5

* Wed Mar 29 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Add 2.4'ish vc/* devices to securetty

* Thu Feb 17 2000 Preston Brown <pbrown@redhat.com>
- add /etc/filesystems with sane defaults

* Wed Feb 16 2000 Bill Nottingham <notting@redhat.com>
- don't set prompt in /etc/profile (it's done in /etc/bashrc)

* Fri Feb  5 2000 Bill Nottingham <notting@redhat.com>
- yet more inputrc tweaks from Hans de Goede (hans@highrise.nl)

* Sun Jan 30 2000 Bill Nottingham <notting@redhat.com>
- yet more inputrc tweaks from Hans de Goede (hans@highrise.nl)

* Sun Jan 23 2000 Bill Nottingham <notting@redhat.com>
- fix mailq line. (#7140)

* Fri Jan 21 2000 Bill Nottingham <notting@redhat.com>
- add ldap to /etc/services

* Tue Jan 18 2000 Bill Nottingham <notting@redhat.com>
- kill HISTFILESIZE, it's broken

* Tue Jan 18 2000 Preston Brown <pbrown@redhat.com>
- some inputrc tweaks

* Wed Jan 12 2000 Bill Nottingham <notting@redhat.com>
- make some more stuff noreplace

* Fri Nov 19 1999 Bill Nottingham <notting@redhat.com>
- fix mailq line. (#7140)

* Fri Oct 29 1999 Bill Nottingham <notting@redhat.com>
- split csh.login into csh.login and csh.cshrc (#various)
- fix pop service names (#6206)
- fix ipv6 protocols entries (#6219)

* Thu Sep  2 1999 Jeff Johnson <jbj@redhat.com>
- rename /etc/csh.cshrc to /etc/csh.login (#2931).
- (note: modified /etc/csh.cshrc should end up in /etc/csh.cshrc.rpmsave)

* Fri Aug 20 1999 Jeff Johnson <jbj@redhat.com>
- add defattr.
- fix limit command in /etc/csh.cshrc (#4582).

* Thu Jul  8 1999 Bill Nottingham <notting@redhat.com>
- move /etc/inputrc here.

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- always use /etc/inputrc

* Wed Mar 31 1999 Preston Brown <pbrown@redhat.com>
- added alias pointing to imap from imap2

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- updated protocols/services from debian to comply with more modern 
- IETF/RFC standards

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Thu Feb 18 1999 Jeff Johnson <jbj@redhat.com>
- unset variables used in /etc/csh.cshrc (#1212)

* Mon Jan 18 1999 Jeff Johnson <jbj@redhat.com>
- compile for Raw Hide.

* Tue Oct 13 1998 Cristian Gafton <gafton@redhat.com>
- fix the csh.cshrc re: ${PATH} undefined

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- /etc/profile uses $i, which needs to be unset

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- made /etc/passwd and /etc/group %config(noreplace)

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- removed /etc/inetd.conf, /etc/rpc
- flagged /etc/securetty as missingok
- fixed buildroot stuff in spec file

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- Don't verify md5sum, size, or timestamp of /var/log/lastlog, /etc/passwd,
  or /etc/group.
