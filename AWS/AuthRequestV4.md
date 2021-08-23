# Auth Requests V4 #

1. Canonical Request
   1. HTTP Verb
   2. Canonical URI
   3. Canonical Query STring
   4. Signed Headers
   5. Hashed Payload
2. String to Sign
   1. AWS4-HMAC-SHA256
   2. Timestamp
   3. Scope
   4. Hex(SHA256Hash(Canonical Request))
3. Signature
   1. Date Key
   2. Date Region Key
   3. Signing Key

## Resources ##

[Header Based Auth Examples of Canonical Request and String to Sign](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-header-based-auth.html)
[Example in Python](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html#sig-v4-examples-get-auth-header)
[How v4 all works together](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-header-based-auth.html)
