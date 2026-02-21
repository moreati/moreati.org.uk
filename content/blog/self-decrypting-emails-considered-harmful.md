---
date: 2009-02-09
title: Self decrypting emails considered harmful
type: post
---

Sending a sensitive file, one that should be encrypted, amongst Linux
and OSS geeks is doable. Most have heard of PGP, many have a GPG key
([here is
mine](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x5A6F95BE "Public PGP key of Alex Willmer"))
and some even use it. Sending an encrypted file to most people is a
non-starter. The software may be there (Outlook is S/MIME capable), but
the knowledge and the experience definately isn't. Which is a shame,
because I'd like to have my bank statement securely sent to my email
account. [PGP Desktop](http://www.pgp.com/products/desktop_home/) has a
feature called the Self Decrypting Archive. To quote the [PGP Command
Line for Servers
FAQ](http://www.pgp.com/products/commandline/servers/#faq17):

> A Self-Decrypting Archive (SDA) is an executable containing a file
> that has been encrypted using a passphrase. A recipient of an SDA runs
> the executable and enters the passphrase to decrypt the file.

SDAs are an attempt to make encrypted email easier, by making decryption
far easier for the recipient. However, Self Decrypting Archives are
fundementally insecure. Here is how they're meant to work:

1.  Alice runs PGP Desktop to encrypt a sensitive file, so she can send
    it to Bob.
2.  Bob doesn't have any encryption software, so PGP Desktop encrypts
    the sensitive file and appends it to a small decryptor program. The
    decryptor + sensitive file is the SDA.
3.  Alice sends the SDA to Bob, attached to an email. Over the phone she
    tells him the encryption key.
4.  Bob receives the email, and runs the SDA.
5.  The SDA requests the decryption key, and decrypts file for Bob.

That sounds great. Alice can encrypt files, send them securely to Bob,
then he can decrypt them. Bob doesn't need any encryption software
installed. Here's the problem: Bob is running an unverified program.
Supposedly it's from Alice, but he can't be sure. This is exactly how
email viruses spread. Bob cannot trust the SDA, since he cannot be sure
what he received was really sent by Alice. Could Alice sign the SDA,
including the decryptor program? Yes, but it won't help. All Bob has to
verify Alice's signature on the SDA, is the decryptor program in that
same SDA. Here's how Mallory, an attacker can subvert this:

1.  Alice sends the encrypted, signed SDA to Bob, and tells Bob the
    encryption key
2.  Mallory intercepts the email, replaces the decryptor program with
    his own. He sends the modified SDA on to Bob, spoofing the from
    address.
3.  Bob receives the email, and runs Mallory's SDA.
4.  Mallory's decryptor, running on Bob's machine fakes a signature
    verification.
5.  Mallory's decryptor requests the encryption key and decrypts the
    file for Bob. It also sends the decrypted file back to Mallory, and
    installs a back door on Bob's computer.

The bottom line, is that you and I must be able to trust our encryption
software, or the encryption is pointless. For that we must be able to
verify we got it from a trustworthy source. Unsigned email, or email
that verifies it's own signature, cannot be trustworthy.
