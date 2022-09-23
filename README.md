# hash-and-salt-your-passwords
Always hash and salt your users passwords for protection against Lookup tables and Rainbow tables
For every application that needs some kind of authentication and authorization, 
a username and password is most likely utilized as the first step for authentication.

Every web developer has had to make a user account system. The problem of storing passwords has been solved by very intelligent folks already.
Ideally, most frameworks already provide a native way of doing that.
The best way to protect user's password is to employ salted password hashing.
This repo is just to document a way of generating secure hashes and random numbers using utilities provided by the python programming language.

Use the secrets module to generate crptographically strong random numbers.
Use the hashlib module to generate secure hashes and message digests.
