import os
import itertools
import string
from tqdm import tqdm
import banner2
import banner1
banner1.bannercat()
banner2.bannerteeth()
def create_wordlist(min_length, max_length, charset, output_dir, chunk_size=10000000):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_index = 0
    count = 0
    total_combinations = sum(len(charset)**i for i in range(min_length, max_length + 1))
    output_file = open(os.path.join(output_dir, f'book{file_index}.txt'), 'w')

    def write_combinations(combinations, pbar):
        nonlocal count, file_index, output_file
        for combination in combinations:
            output_file.write(''.join(combination) + '\n')
            count += 1
            pbar.update(1)
            
            if count % chunk_size == 0:
                output_file.close()
                file_index += 1
                output_file = open(os.path.join(output_dir, f'book{file_index}.txt'), 'w')
    
    with tqdm(total=total_combinations, unit="comb") as pbar:
        for length in range(min_length, max_length + 1):
            combinations = itertools.product(charset, repeat=length)
            write_combinations(combinations, pbar)

    output_file.close()

if __name__ == "__main__":
    min_length = int(input("Oluşturulacak kelimelerin minimum uzunluğu (örneğin, 4): "))
    max_length = int(input("Oluşturulacak kelimelerin maksimum uzunluğu (örneğin, 8): "))
    output_dir = 'books'
    
    print("Seçenekler:")
    print("1: Sadece sayılar (numeric)")
    print("2: Sayılar ve harfler (alphanumeric)")
    print("3: Sayılar, harfler ve özel karakterler (special characters)")
    
    choice = int(input("Seçiminizi yapın (1, 2 veya 3): "))
    
    if choice == 1:
        charset = string.digits
    elif choice == 2:
        charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif choice == 3:
        extra_chars = input("Eklemek istediğiniz özel karakterleri girin (örneğin, @#₺&): ")
        charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + extra_chars
    else:
        print("Geçersiz seçim!")
        exit(1)
    
    create_wordlist(min_length, max_length, charset, output_dir)
