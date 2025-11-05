import os
import json
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

# =========================
# Fungsi transformasi angka
# =========================
def transform_number(num: str) -> str:
    if len(num) < 3:
        raise ValueError("Minimal panjang angka 3 digit")

    left = num[:-3]
    ratusan = int(num[-3])
    puluhan = int(num[-2])
    satuan = int(num[-1])

    puluhan_new = puluhan - 1
    borrow = 0
    if puluhan_new < 0:
        puluhan_new = 9
        borrow = 1

    ratusan_new = ratusan - borrow
    if ratusan_new < 0:
        ratusan_new = 9

    if puluhan == 5:
        satuan_new = (satuan + 3) % 10
    else:
        satuan_new = (satuan + 2) % 10

    return left + str(ratusan_new) + str(puluhan_new) + str(satuan_new)


# =========================
# Kelas utama tampilan Kivy
# =========================
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        # Input angka
        self.input_field = TextInput(
            hint_text="Masukkan angka minimal 3 digit...",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.input_field)

        # Tombol Mulai
        self.btn_mulai = Button(
            text="Mulai",
            size_hint_y=None,
            height=50,
            on_press=self.on_mulai
        )
        self.add_widget(self.btn_mulai)

        # Tombol Proses (kosong sementara)
        self.btn_proses = Button(
            text="Proses",
            size_hint_y=None,
            height=50,
            on_press=self.on_proses
        )
        self.add_widget(self.btn_proses)

        # Area hasil
        self.result_area = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.result_area.bind(minimum_height=self.result_area.setter('height'))

        scroll = ScrollView()
        scroll.add_widget(self.result_area)
        self.add_widget(scroll)

        # Data hasil
        self.results = []

        # Pastikan folder hasil ada
        self.output_dir = os.path.join(os.getcwd(), "hasil")
        os.makedirs(self.output_dir, exist_ok=True)

    def on_mulai(self, instance):
        val = self.input_field.text.strip()
        if not val.isdigit():
            self.add_result("⚠️ Input harus angka")
            return
        if len(val) < 3:
            self.add_result("⚠️ Minimal 3 digit")
            return

        # Jalankan 100 kali transformasi
        start_time = time.time()
        current = val
        all_results = []

        for i in range(1, 101):
            current = transform_number(current)
            all_results.append({"Iterasi": i, "Angka": current})

        elapsed = time.time() - start_time
        self.results = all_results[-10:]

        # Simpan hasil ke file
        self.save_results(all_results)

        # Update tampilan
        self.result_area.clear_widgets()
        self.add_result("═" * 35)
        self.add_result("📊 10 Hasil Terakhir:")
        self.add_result("═" * 35)

        for r in self.results:
            lbl = Label(
                text=f"#{r['Iterasi']:03d} ➜ {r['Angka']}",
                size_hint_y=None,
                height=30
            )
            self.result_area.add_widget(lbl)

        self.add_result(f"✅ Selesai dalam {elapsed:.2f} detik")
        self.add_result(f"💾 Hasil disimpan di folder: hasil/")

    def save_results(self, all_results):
        """Simpan hasil ke JSON dan Excel"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        json_path = os.path.join(self.output_dir, f"hasil_generate_{timestamp}.json")
        xlsx_path = os.path.join(self.output_dir, f"hasil_generate_{timestamp}.xlsx")

        # Simpan JSON
        try:
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(all_results, f, indent=2, ensure_ascii=False)
            self.add_result(f"💾 JSON: {os.path.basename(json_path)}")
        except Exception as e:
            self.add_result(f"⚠️ Gagal simpan JSON: {e}")

        # Simpan Excel
        try:
            from openpyxl import Workbook
            wb = Workbook()
            ws = wb.active
            ws.title = "Hasil Generate"
            ws.append(["Iterasi", "Angka"])
            for row in all_results:
                ws.append([row["Iterasi"], row["Angka"]])
            wb.save(xlsx_path)
            self.add_result(f"💾 Excel: {os.path.basename(xlsx_path)}")
        except Exception as e:
            self.add_result(f"⚠️ Gagal simpan Excel: {e}")

    def on_proses(self, instance):
        self.add_result("Fungsi 'Proses' belum diimplementasikan")

    def add_result(self, text):
        lbl = Label(text=text, size_hint_y=None, height=30)
        self.result_area.add_widget(lbl)


class TransformApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    TransformApp().run()
