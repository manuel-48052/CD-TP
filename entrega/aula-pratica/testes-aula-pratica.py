import aulapratica

def test_a() -> None:
    print("u = 2, r = 2, N = 4")
    aulapratica.geometric_progression(2, 2, 4)
    print("u = 2, r = 4, N = 5")
    aulapratica.geometric_progression(2, 4, 5)
    print("u = 4, r = 1, N = 4")
    aulapratica.geometric_progression(3, 1, 4)

def test_b() -> None:
    print(f"gcd(128,3) = {aulapratica.mdc_euclides(128, 3)}")
    print(f"gcd(2750,20) = {aulapratica.mdc_euclides(2750, 20)}")
    print(f"gcd(14,0) = {aulapratica.mdc_euclides(14, 0)}")
    print(f"gcd(7,7) = {aulapratica.mdc_euclides(7, 7)}")


def test_c() -> None:
    aulapratica.most_least_frequent_symbols("a.txt")
    aulapratica.most_least_frequent_symbols("ListaPalavrasPT.txt")

def test_d() -> None:
    aulapratica.histograma_entropia("a.txt")


if __name__ == '__main__':
    print("Test a)")
    test_a()
    print("Test b)")
    test_b()
    print("Test c)")
    test_c()
    print("Test d)")
    test_d()
