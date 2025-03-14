import liboqs

def main():
    # Initialize Kyber encryption
    kem = liboqs.KeyEncapsulation("Kyber512")  # Choose Kyber512, Kyber768, or Kyber1024

    # Generate key pair (public and private)
    print("Generating key pair...")
    public_key = kem.generate_keypair()
    secret_key = kem.export_secret_key()

    # Message to be encrypted (converted to bytes)
    message = "Hello, world!".encode("utf-8")

    # Encrypt the message
    print("Encrypting the message...")
    ciphertext, shared_secret_enc = kem.encap_secret(public_key)

    # Decrypt the message
    print("Decrypting the message...")
    shared_secret_dec = kem.decap_secret(ciphertext)

    # Verify if shared secrets match
    if shared_secret_enc == shared_secret_dec:
        print("Success! Shared secrets match.")
        print(f"Original message: {message.decode('utf-8')}")
        print(f"Encrypted shared secret: {shared_secret_enc.hex()}")
    else:
        print("Error: Shared secrets do not match.")

    # Free memory
    kem.free()

if __name__ == "__main__":
    main()