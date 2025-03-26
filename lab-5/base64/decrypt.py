import base64

def main():
    try:
        with open("DuLieu.txt", "r") as file:
            encoded_string = file.read().strip()
            
        decoded_bytes = base64.b64decode(encoded_string)
        decode_string = decoded_bytes.decode("utf-8")
        
        print("Chuỗi sau khi giải mã:", decode_string)
    except Exception as e:
        print("lỗi:", e)
        
if __name__ == "__main__":
    main()