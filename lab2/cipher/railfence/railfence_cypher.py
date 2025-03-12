class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plaintext, num_rails):
        # Create the rails (list of lists)
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up
        
        # Encrypt the plaintext by placing characters in the correct rails
        for char in plaintext:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        # Combine the rails into a single string for the ciphertext
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Calculate the lengths of characters in each rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        
        # Calculate the number of characters in each rail
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Split the ciphertext into the rails
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length
        
        # Decrypt the message by reading the rails in the correct order
        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index].pop(0)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        return plain_text                      