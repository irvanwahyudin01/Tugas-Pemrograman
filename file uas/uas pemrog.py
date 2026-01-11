class Feedback:
    def __init__(self, nama, rating):
        self.nama = nama
        self.rating = rating

class FeedbackService:
    def __init__(self):
        self.data_feedback = []

    def tambah_feedback(self, feedback):
        self.data_feedback.append(feedback)

    def rata_rata_rating(self):
        if len(self.data_feedback) == 0:
            return 0
        total = sum(f.rating for f in self.data_feedback)
        return total / len(self.data_feedback)

    def kategori_kepuasan(self, rating):
        if rating >= 4:
            return "Sangat Puas"
        elif rating >= 3:
            return "Puas"
        elif rating >= 2:
            return "Cukup"
        else:
            return "Tidak Puas"
        
class FeedbackView:
    def input_feedback(self):
        nama = input("Masukkan nama pelanggan: ")

        while True:
            try:
                rating = int(input("Masukkan rating (1-5): "))
                if rating < 1 or rating > 5:
                    raise ValueError
                return Feedback(nama, rating)
            except ValueError:
                print("Rating harus angka 1 sampai 5!")

    def tampilkan_tabel(self, data_feedback, service):
        print("\n=== TABEL KEPUASAN PELANGGAN ===")
        print("-" * 45)
        print(f"{'No':<5}{'Nama':<20}{'Rating':<10}{'Kategori'}")
        print("-" * 45)

        for i, f in enumerate(data_feedback, start=1):
            kategori = service.kategori_kepuasan(f.rating)
            print(f"{i:<5}{f.nama:<20}{f.rating:<10}{kategori}")

        print("-" * 45)
        print(f"Rata-rata Rating : {service.rata_rata_rating():.2f}")

def main():
    service = FeedbackService()
    view = FeedbackView()

    while True:
        feedback = view.input_feedback()
        service.tambah_feedback(feedback)

        lanjut = input("Tambah data lagi? (y/n): ").lower()
        if lanjut != 'y':
            break

    view.tampilkan_tabel(service.data_feedback, service)


if __name__ == "__main__":
    main()
