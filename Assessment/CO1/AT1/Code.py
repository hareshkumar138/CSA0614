def image_processing(size):
    if size <= 1:
        return
    print(f"Processing image of size {size} x {size}")
    new_size = size // 2
    image_processing(new_size) 
    image_processing(new_size)
    image_processing(new_size)
    image_processing(new_size)
    print(f"Combining four quadrants of size {new_size} x {new_size}")
image_size = 8
image_processing(image_size)
