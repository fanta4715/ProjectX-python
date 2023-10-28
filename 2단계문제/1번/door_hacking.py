import zipfile
import time

def unlock_zip(zip_filename):
    start_time = time.time()
    zip_file = zipfile.ZipFile(zip_filename)
    password = ""
    max_length = 6
    characters = "0123456789abcdefghijklmnopqrstuvwxyz"
    attempt_count = 0

    while len(password) <= max_length:
        for char in characters:
            attempt = password + char
            attempt_count += 1
            print(f"attemp:{password}")
            try:
                zip_file.extractall(pwd=attempt.encode('utf-8'))
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Password found: {attempt}")
                print(f"Elapsed time: {elapsed_time:.2f} seconds")
                print(f"Attempt count: {attempt_count}")
                with open("password.txt", "w") as password_file:
                    password_file.write(attempt)
                return

            except Exception:
                # 암호가 틀릴 경우 예외가 발생함
                pass

        password = increment_password(password, characters)

def increment_password(password, characters):
    # 암호를 증가시키는 함수
    if password == "":
        return characters[0]

    last_char = password[-1]
    if last_char == characters[-1]:
        return increment_password(password[:-1], characters) + characters[0]
    else:
        index = characters.index(last_char)
        return password[:-1] + characters[index + 1]

if __name__ == "__main__":
    zip_filename = "emergency_storage_key.zip"
    unlock_zip(zip_filename)
