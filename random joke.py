import random

FIKRALAR = [
    "Temel bir gün bakkala girmiş: 'Abi, uzaktan kumandalı ekmek var mı?' Bakkal: 'Yok.' Temel: 'O zaman şu normal ekmeği ver, kanal değiştirmeye çalışırım.'",
    "Programcı neden gözlük takar? Çünkü C# göremez!",
    "Doktor hastaya: 'Size kötü bir haberim var.' Hasta: 'Nedir?' Doktor: 'Faturayı gördünüz mü?'",
    "Nasreddin Hoca'ya sormuşlar: 'Ay mı daha faydalı, güneş mi?' Hoca: 'Ay. Çünkü karanlıkta lazım, güneş zaten gündüz var.'",
    "Bilgisayar neden soğuk almaz? Çünkü Windows'u hep açıktır ama Pencere kapalıdır... Ya da Fan'ı vardır!",
    "Öğretmen: 'Ali, 5 elmadan 2 tanesini yersen kaç kalır?' Ali: 'Karnım doyar öğretmenim.'",
    "Bug nedir? Programcının 'bu bir özellik' dediği şey.",
]

def main():
    print("😂 RASTGELE FIKRA ÜRETİCİ 😂")
    while True:
        input("\nFıkra için Enter'a bas (çıkmak için Ctrl+C)...")
        print("\n" + random.choice(FIKRALAR))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGörüşürüz!")