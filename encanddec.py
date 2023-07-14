try:
    message = input("Enter a message to encrypt: ")
    enc_message = ""
    for word in message:
        enc_message += chr(ord(word) + 1) 
    print("Encrypted Message:", enc_message)

    dec_message = ""
    for word in enc_message:
        dec_message += chr(ord(word) - 1)  
    print("Decrypted Message:", dec_message)

except:
    print("An error occurred in the program.")