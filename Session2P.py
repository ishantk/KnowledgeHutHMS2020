"""
    Image is a Collection of Pixels
    Pixel is Collection of RGB Values
"""
#         R    G    B
pixel1 = [120, 50, 90]
pixel2 = [220, 50, 90]
pixel3 = [140, 50, 90]
pixel4 = [110, 50, 90]
pixel5 = [190, 50, 90]
pixel6 = [180, 50, 90]
pixel7 = [210, 50, 90]
pixel8 = [180, 50, 90]
pixel9 = [201, 50, 90]

image = [
    [pixel1, pixel2, pixel3],   #0
    [pixel4, pixel5, pixel6],   #1
    [pixel7, pixel8, pixel9],   #2
]
print(image)
print(type(image))

print(len(image))        #3

print(image[0])
print(len(image[0]))     #3

print(image[0][0])       # [120, 50, 90]
print(image[0][0][0])    # 120


"""
    Assignment:
    Image Rotation:
    image = [
        [pixel1, pixel2, pixel3],  
        [pixel4, pixel5, pixel6],   
        [pixel7, pixel8, pixel9],   
    ]
    
    Final Output after you process the above image
    
    rotated_image = [
        [pixel1, pixel4, pixel7],
        [pixel2, pixel5, pixel8],
        [pixel3, pixel6, pixel9],
    ]
"""

