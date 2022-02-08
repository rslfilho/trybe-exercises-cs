def triangle_type(face1, face2, face3):
    is_triangle = (
        face1 + face2 > face3 and
        face2 + face3 > face1 and
        face1 + face3 > face2
    )

    if not is_triangle:
        return "não é triângulo"
    elif face1 == face2 == face3:
        return "Triângulo Equilátero"
    elif face1 == face2 or face1 == face3 or face2 == face3:
        return "Triângulo Isósceles"
    else:
        return "Triângulo escaleno"


print(triangle_type(2, 3, 4))
