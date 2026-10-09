"""Original bilingual editorial copy. Keep claims tied to the cited source IDs."""

ARTICLES = [
    {
        "slug": "watt-dan-kwh",
        "id": {
            "title": "Watt dan kWh: daya berbeda dari energi",
            "summary": "Kenali perbedaan angka pada label perangkat dan angka pada meter listrik sebelum menghitung biaya.",
            "sections": [
                ("Watt menunjukkan laju", "Watt (W) menyatakan seberapa cepat perangkat menggunakan energi pada suatu saat. Angka 100 W bukan berarti perangkat selalu memakai 100 kWh. Untuk membandingkan dua perangkat, catat juga berapa lama masing-masing bekerja dan apakah dayanya tetap atau berubah. Label daya sering menunjukkan nilai nominal, bukan hasil pengukuran sepanjang hari."),
                ("kWh menjumlahkan penggunaan", "Kilowatt-jam (kWh) adalah satuan energi. Jika beban stabil 1.000 W bekerja satu jam, penggunaannya 1 kWh. Beban 100 W yang bekerja sepuluh jam juga memakai 1 kWh. Karena itu, perangkat berdaya kecil yang menyala terus bisa memakai energi lebih banyak daripada perangkat besar yang hanya dipakai sebentar."),
                ("Gunakan satuan yang sama", "Ubah watt menjadi kilowatt dengan membagi 1.000, lalu kalikan dengan jam. Jika yang tersedia adalah angka kWh tahunan pada label, jangan kalikan lagi dengan jam: angka itu sudah menyatakan energi selama periode label. Periksa selalu periode dan kondisi pengujian yang tercetak pada label."),
            ],
            "example": "Contoh: lampu 10 W selama 5 jam memakai 10 × 5 ÷ 1.000 = 0,05 kWh. Ini contoh matematika, bukan pengukuran sebuah produk.",
            "pitfall": "Kesalahan umum: menyebut perangkat 100 W memakai 100 kWh tanpa menyatakan waktu pemakaian.",
        },
        "en": {
            "title": "Watts and kWh: power is different from energy",
            "summary": "Understand the difference between the number on an appliance label and the number on your electricity meter.",
            "sections": [
                ("Watts describe a rate", "Watts (W) tell you how quickly a device uses energy at a moment in time. A 100 W rating does not mean the device always uses 100 kWh. To compare devices, you also need operating time and an idea of whether the power draw stays constant. A rating plate is often a nominal value, not a measurement over a whole day."),
                ("kWh add up energy", "A kilowatt-hour (kWh) is a unit of energy. A steady 1,000 W load running for one hour uses 1 kWh. A 100 W load running for ten hours also uses 1 kWh. A small load left on continuously can therefore use more energy than a powerful device used briefly."),
                ("Keep the units straight", "Convert watts to kilowatts by dividing by 1,000, then multiply by hours. If a label already states annual kWh, do not multiply it by hours again: it already reports energy for the stated period. Read the test period and conditions on the label."),
            ],
            "example": "Example: a 10 W lamp used for 5 hours consumes 10 × 5 ÷ 1,000 = 0.05 kWh. This is arithmetic, not a product measurement.",
            "pitfall": "Common error: saying a 100 W device consumes 100 kWh without specifying operating time.",
        },
        "sources": ["eia", "nist"],
    },
    {
        "slug": "membaca-label-daya",
        "id": {
            "title": "Membaca label daya tanpa salah tafsir",
            "summary": "Temukan angka yang tepat pada spesifikasi perangkat dan pahami mengapa angka label belum tentu sama dengan pemakaian nyata.",
            "sections": [
                ("Cari daya masuk", "Untuk perkiraan konsumsi listrik, cari daya listrik masuk dalam W atau kW pada label, manual, atau lembar spesifikasi. Jangan langsung memakai angka kapasitas keluaran, misalnya tingkat kecerahan lampu atau kapasitas pendinginan. Keduanya menggambarkan hasil kerja perangkat, bukan selalu daya listrik yang ditarik dari stopkontak."),
                ("Perhatikan mode operasi", "Satu perangkat dapat memiliki beberapa tingkat daya: aktif, siaga, dan mati tetapi tetap terhubung. Perangkat yang memanas atau mendingin dapat hidup-mati otomatis. Angka maksimum pada label berguna untuk memahami batas, tetapi dapat melebihkan perkiraan energi jika dipakai seolah-olah berlaku setiap menit."),
                ("Ukur bila keputusan penting", "Jika ingin membandingkan biaya nyata, pengukur energi colokan dapat mencatat kWh selama beberapa hari untuk perangkat yang sesuai. Ikuti petunjuk keselamatan alat ukur dan jangan memasang perangkat yang melebihi kapasitasnya. Bandingkan hasil pengukuran pada pola pemakaian yang serupa."),
            ],
            "example": "Contoh: label 800 W pada sebuah alat tidak membuktikan alat itu menarik 800 W selama 24 jam. Gunakan jam kerja sebenarnya atau hasil pengukuran kWh.",
            "pitfall": "Kesalahan umum: memakai angka kapasitas keluaran sebagai watt listrik masuk.",
        },
        "en": {
            "title": "Reading an appliance power label accurately",
            "summary": "Find the relevant input rating and see why a label is not the same as a real-world energy measurement.",
            "sections": [
                ("Look for electrical input", "For an electricity estimate, find input power in W or kW on the rating plate, manual, or specification sheet. Do not substitute an output figure such as brightness or cooling capacity. Those describe what a device delivers, not necessarily what it draws from an outlet."),
                ("Account for operating modes", "A device may draw different power when active, on standby, or apparently off but still plugged in. Heating and cooling appliances can cycle automatically. A maximum rating can help identify an upper operating limit but may exaggerate energy use if treated as the draw at every minute."),
                ("Measure when it matters", "A suitable plug-in energy meter can record kWh over several days for a device you want to compare. Follow the meter's safety instructions and stay within its capacity. Compare readings under similar usage patterns."),
            ],
            "example": "Example: an 800 W label does not establish that the appliance draws 800 W all day. Use actual run time or measured kWh.",
            "pitfall": "Common error: treating an output capacity figure as electrical input watts.",
        },
        "sources": ["eia", "standby"],
    },
    {
        "slug": "hitung-kwh-bulanan",
        "id": {
            "title": "Mengubah jam pemakaian menjadi kWh bulanan",
            "summary": "Susun perkiraan yang bisa diperiksa: watt, jam per hari, hari pemakaian, lalu hasil kWh.",
            "sections": [
                ("Mulai dari satu perangkat", "Rumus untuk beban yang relatif tetap adalah watt × jam per hari × hari pemakaian ÷ 1.000. Jika ada beberapa perangkat yang sama, kalikan jumlah unitnya. Catat apakah jam yang dipakai merupakan jadwal harian, rata-rata mingguan, atau tebakan; hasil akan mengikuti mutu masukan."),
                ("Jangan memaksakan 30 hari", "Alat yang digunakan hanya pada hari kerja mungkin aktif sekitar 20 hari, sedangkan kulkas terhubung sepanjang bulan tetapi kompresornya tidak selalu aktif. Masukkan hari yang masuk akal untuk pola Anda. Untuk tagihan, ikuti jumlah hari pada periode penagihan yang sesungguhnya."),
                ("Pisahkan kWh dari uang", "kWh adalah perkiraan energi. Untuk perkiraan biaya energi, kalikan hasil kWh dengan tarif per kWh yang Anda ketahui. Pajak, biaya tetap, subsidi, tarif bertingkat, dan aturan lokal dapat membuat angka pada tagihan berbeda. Kalkulator kami tidak menggantikan rincian penyedia listrik."),
            ],
            "example": "Contoh: kipas 50 W × 8 jam/hari × 25 hari ÷ 1.000 = 10 kWh. Jika dua kipas identik dipakai sama lama, hasilnya 20 kWh.",
            "pitfall": "Kesalahan umum: mengalikan watt dengan hari tetapi lupa mengalikan jam atau membagi 1.000.",
        },
        "en": {
            "title": "Turn operating hours into monthly kWh",
            "summary": "Build an estimate you can check: watts, hours per day, days of use, then kWh.",
            "sections": [
                ("Start with one device", "For a fairly steady load, use watts × hours per day × days used ÷ 1,000. Multiply by quantity if several identical devices follow the same schedule. Record whether your hours are a daily schedule, a weekly average, or a guess; the output can only be as good as the inputs."),
                ("Do not force 30 days", "A device used only on workdays may run around 20 days, while a refrigerator stays connected all month but its compressor does not run continuously. Enter days that fit your own pattern. For bill comparisons, use the actual number of days in the billing period."),
                ("Separate kWh from money", "kWh estimate energy. To estimate the energy charge, multiply kWh by a rate you know. Taxes, fixed fees, subsidies, tiered rates, and local rules can make the bill differ. Our calculator does not replace your provider's itemized statement."),
            ],
            "example": "Example: a 50 W fan × 8 hours/day × 25 days ÷ 1,000 = 10 kWh. Two identical fans on the same schedule use an estimated 20 kWh.",
            "pitfall": "Common error: multiplying watts by days while forgetting hours or the division by 1,000.",
        },
        "sources": ["eia", "aus"],
    },
    {
        "slug": "membaca-tagihan",
        "id": {
            "title": "Membaca tagihan listrik sebelum membandingkan biaya",
            "summary": "Pisahkan energi, periode, tarif, dan biaya lain agar perbandingan dua bulan lebih adil.",
            "sections": [
                ("Mulai dari periode dan kWh", "Cari tanggal awal dan akhir pembacaan serta total kWh pada masing-masing tagihan. Bulan dengan lebih banyak hari dapat menghasilkan kWh lebih tinggi tanpa perubahan kebiasaan. Jika perlu, bagi kWh dengan jumlah hari untuk memperoleh rata-rata harian sebelum membandingkan dua periode."),
                ("Periksa komponen pembayaran", "Tagihan dapat berisi tarif energi, biaya tetap, pajak, penyesuaian, atau potongan. Struktur setiap penyedia dan wilayah berbeda. Karena itu, membagi jumlah akhir tagihan dengan kWh tidak selalu memberi tarif energi murni. Pakai tarif dari dokumen penyedia atau masukkan angka sebagai perkiraan pribadi yang jelas."),
                ("Cari penyebab sebelum bertindak", "Perubahan cuaca, jumlah penghuni, jam bekerja di rumah, perangkat baru, dan siklus penagihan dapat mengubah kWh. Catat konteks ini bersama angka. Satu tagihan yang tinggi belum cukup untuk menyimpulkan ada perangkat yang rusak atau kesalahan meter."),
            ],
            "example": "Contoh: 210 kWh dalam 30 hari berarti 7 kWh/hari; 224 kWh dalam 32 hari juga 7 kWh/hari. Total berbeda, rata-rata sama.",
            "pitfall": "Kesalahan umum: membandingkan total pembayaran tanpa melihat jumlah hari dan rincian biaya.",
        },
        "en": {
            "title": "Read your electricity bill before comparing costs",
            "summary": "Separate energy, billing period, rate, and other charges for a fairer comparison.",
            "sections": [
                ("Start with dates and kWh", "Find the start and end of the meter-reading period and the total kWh on each bill. A longer billing period can produce more kWh even when habits are unchanged. Divide kWh by the number of days to compare daily averages across different periods."),
                ("Inspect the charges", "Bills may include an energy rate, fixed charges, taxes, adjustments, or discounts. Structures differ by provider and location. Dividing the final amount due by kWh therefore does not always reveal the energy-only rate. Use your provider's stated rate or label an entered value as your own approximation."),
                ("Find context before acting", "Weather, occupancy, time spent at home, a new appliance, and the billing cycle can all change kWh. Record these factors alongside the numbers. One unusually high bill alone does not prove a faulty appliance or meter."),
            ],
            "example": "Example: 210 kWh over 30 days is 7 kWh/day; 224 kWh over 32 days is also 7 kWh/day. Totals differ, daily averages match.",
            "pitfall": "Common error: comparing the final amount due without checking billing days and charge details.",
        },
        "sources": ["eia", "aus"],
    },
    {
        "slug": "daya-siaga",
        "id": {
            "title": "Daya siaga: kecil per jam, lama dalam pemakaian",
            "summary": "Pelajari cara memperkirakan energi perangkat yang tetap terhubung saat tidak digunakan.",
            "sections": [
                ("Kenali mode siaga", "Beberapa perangkat tetap mengambil daya saat tampak mati: misalnya untuk jam, penerima sinyal, atau kesiapan memulai. Ini disebut daya siaga. Nilainya berbeda menurut model dan mode. Jangan mengambil satu angka internet lalu menganggap semua perangkat memiliki daya siaga yang sama."),
                ("Hitung dengan waktu yang tepat", "Jika daya siaga terukur 2 W selama 20 jam sehari dan 30 hari, energinya 2 × 20 × 30 ÷ 1.000 = 1,2 kWh. Jangan menghitung 24 jam siaga bila perangkat aktif empat jam; pisahkan kedua mode lalu jumlahkan. Untuk hasil lebih baik, ukur dalam beberapa hari."),
                ("Pertimbangkan fungsi dan keamanan", "Memutus daya dari sebuah perangkat dapat menghilangkan pengaturan atau fungsi yang memang diperlukan. Jangan memutus perangkat keselamatan atau layanan penting hanya demi penghematan kecil. Pengukuran dan keputusan harus mengikuti petunjuk produsen serta kondisi rumah."),
            ],
            "example": "Contoh: 2 W × 20 jam × 30 hari ÷ 1.000 = 1,2 kWh untuk satu perangkat pada asumsi tersebut.",
            "pitfall": "Kesalahan umum: menganggap semua colokan memiliki daya siaga atau semua daya siaga bisa dihilangkan tanpa konsekuensi.",
        },
        "en": {
            "title": "Standby power: small each hour, long in use",
            "summary": "Estimate the energy drawn by devices that stay connected while they are not in active use.",
            "sections": [
                ("Recognize standby mode", "Some products still draw power when they appear off, perhaps for a clock, receiver, or quick start. This is standby power. The amount varies by model and mode. An online figure for one device should not be applied to every product."),
                ("Use the right number of hours", "If measured standby draw is 2 W for 20 hours a day over 30 days, energy is 2 × 20 × 30 ÷ 1,000 = 1.2 kWh. Do not count 24 standby hours if the device is active for four; estimate the modes separately and add them. A multi-day measurement is better when practical."),
                ("Keep function and safety in mind", "Disconnecting a device may remove settings or a function you need. Do not switch off a safety device or an essential service for a small estimated saving. Follow product instructions and consider your household's needs."),
            ],
            "example": "Example: 2 W × 20 hours × 30 days ÷ 1,000 = 1.2 kWh for one device under those assumptions.",
            "pitfall": "Common error: assuming every plug has the same standby draw or can be disconnected without consequences.",
        },
        "sources": ["standby"],
    },
    {
        "slug": "bandingkan-lampu",
        "id": {
            "title": "Membandingkan lampu dengan kebutuhan cahaya yang sama",
            "summary": "Gunakan lumen untuk kebutuhan cahaya dan watt untuk biaya energi; jangan membandingkan watt saja.",
            "sections": [
                ("Samakan layanan yang diterima", "Lampu dengan watt lebih rendah belum tentu cocok jika cahayanya terlalu redup. Tentukan kebutuhan ruangan, lalu bandingkan angka lumen, arah cahaya, dan penggunaan yang sama. Watt menunjukkan daya masuk; lumen menunjukkan keluaran cahaya tampak. Perhatikan juga warna cahaya dan kompatibilitas fitting."),
                ("Hitung selisih energinya", "Setelah dua pilihan memberikan cahaya yang sebanding, kurangi watt lampu baru dari watt lampu lama. Kalikan selisih dengan jam per hari, hari, dan jumlah lampu, lalu bagi 1.000. Hasilnya perkiraan selisih kWh pada jadwal yang Anda masukkan, bukan janji penghematan untuk setiap rumah."),
                ("Lihat lebih dari tagihan", "Harga beli, masa pakai, dan kecocokan sakelar juga memengaruhi keputusan. Jika lampu lama masih berfungsi, Anda bisa memulai dari ruangan yang paling sering digunakan. Jangan menyatakan waktu balik modal tanpa harga nyata dan jam penggunaan yang benar."),
            ],
            "example": "Contoh: selisih 40 W selama 4 jam sehari, 30 hari, pada 3 lampu = 40 × 4 × 30 × 3 ÷ 1.000 = 14,4 kWh.",
            "pitfall": "Kesalahan umum: membandingkan lampu hanya dari watt tanpa memastikan keluaran cahaya yang setara.",
        },
        "en": {
            "title": "Compare lamps that provide similar light",
            "summary": "Use lumens for the light you need and watts for energy; watts alone are not a fair comparison.",
            "sections": [
                ("Match the service", "A lower-watt lamp is not necessarily suitable if it leaves the room too dim. Decide what light the space needs, then compare lumens, beam direction, and the same usage schedule. Watts describe input power; lumens describe visible light output. Also check color preference and socket compatibility."),
                ("Calculate the energy difference", "Once two choices provide comparable light, subtract the new lamp's watts from the old lamp's watts. Multiply by hours per day, days, and the number of lamps, then divide by 1,000. The result estimates a kWh difference for your entered schedule, not a promised saving for every home."),
                ("Look beyond the bill", "Purchase price, expected life, and switch compatibility also matter. If the existing lamp still works, you may start with the most frequently used rooms. Do not claim a payback period without real prices and usage hours."),
            ],
            "example": "Example: a 40 W difference for 4 hours/day, 30 days, across 3 lamps is 40 × 4 × 30 × 3 ÷ 1,000 = 14.4 kWh.",
            "pitfall": "Common error: comparing lamps only by watts without checking that they provide comparable light.",
        },
        "sources": ["lighting", "eia"],
    },
    {
        "slug": "perangkat-berdaya-berubah",
        "id": {
            "title": "Mengapa kulkas dan pendingin ruangan sulit dihitung dari label",
            "summary": "Kenali perangkat yang dayanya berubah menurut siklus, suhu, dan setelan sehingga perkiraan sederhana perlu diberi batas.",
            "sections": [
                ("Siklus bukan jam penuh", "Kompresor kulkas dan pendingin ruangan dapat menyala dan berhenti otomatis. Banyak perangkat modern juga mengubah kecepatannya. Mengalikan daya maksimum dengan 24 jam biasanya bukan gambaran pemakaian yang sebenarnya. Suhu lingkungan, setelan, ukuran ruang, kondisi pintu, dan perawatan ikut berpengaruh."),
                ("Pilih data yang sesuai", "Jika tersedia angka kWh per periode pada label energi, gunakan angka tersebut dengan memahami kondisi uji resminya. Jika ingin tahu pemakaian di rumah sendiri, pengukuran kWh selama periode yang mewakili kebiasaan Anda lebih berguna daripada satu pembacaan watt sesaat. Hindari membandingkan hari yang berbeda jauh cuacanya."),
                ("Jelaskan rentang ketidakpastian", "Perkiraan dari watt × jam tetap berguna sebagai ilustrasi batas atas pada asumsi tertentu, bukan tagihan yang pasti. Beri nama asumsi, catat sumber watt, dan perbarui perkiraan setelah mendapat pengukuran. Jangan memakai hasil kalkulator untuk mendiagnosis kerusakan perangkat."),
            ],
            "example": "Contoh: label 900 W tidak berarti 900 × 24 ÷ 1.000 = 21,6 kWh setiap hari. Persamaan itu hanya berlaku jika daya 900 W benar-benar konstan sepanjang 24 jam.",
            "pitfall": "Kesalahan umum: menganggap angka watt maksimum sebagai rata-rata untuk perangkat yang bersiklus.",
        },
        "en": {
            "title": "Why a refrigerator or air conditioner is hard to estimate from its label",
            "summary": "Understand cycling and variable power before treating a simple watt-hour estimate as a bill prediction.",
            "sections": [
                ("A cycle is not full-time draw", "Refrigerator and air-conditioner compressors can start and stop automatically. Many modern units also vary their speed. Multiplying maximum watts by 24 hours is usually not a realistic account of their use. Ambient temperature, settings, room size, door opening, and maintenance all affect the outcome."),
                ("Choose suitable data", "If an energy label states kWh over a period, use that figure while noting its official test conditions. To learn about your own home, a kWh measurement over a representative period is more useful than one momentary watt reading. Avoid comparing days with very different weather."),
                ("Describe uncertainty", "Watts × hours can still illustrate a bound under a stated assumption, but it is not a guaranteed bill. Name the assumptions, record where the watt figure came from, and revise the estimate when you have measurements. Do not use a calculator result to diagnose equipment faults."),
            ],
            "example": "Example: a 900 W rating does not mean 900 × 24 ÷ 1,000 = 21.6 kWh every day. That equation applies only if the device actually draws 900 W continuously for 24 hours.",
            "pitfall": "Common error: using maximum rated watts as the average for an appliance that cycles.",
        },
        "sources": ["aus", "eia"],
    },
    {
        "slug": "audit-rumah",
        "id": {
            "title": "Audit pemakaian listrik rumah dalam satu lembar",
            "summary": "Buat daftar kecil yang bisa diperbaiki dari waktu ke waktu, tanpa menebak perangkat penyebab tagihan.",
            "sections": [
                ("Catat yang dapat diperiksa", "Mulai dengan nama perangkat, jumlah unit, daya dari label atau meter, jam aktif per hari, hari pemakaian, dan sumber angkanya. Beri tanda pada nilai yang masih tebakan. Anda tidak perlu mendaftar setiap colokan pada hari pertama; mulailah dengan perangkat yang sering atau lama dipakai."),
                ("Pisahkan jenis perkiraan", "Untuk beban stabil, hitung watt × jam × hari ÷ 1.000. Untuk perangkat yang dayanya berubah, pakai data kWh pada label atau hasil meter bila tersedia. Untuk siaga, catat jam siaga terpisah dari jam aktif. Penjumlahan baru masuk akal jika periode setiap perangkat sama."),
                ("Bandingkan dengan meter utama", "Jumlah perkiraan perangkat bisa berbeda dari total meter karena ada beban yang terlewat, nilai label yang tidak sama dengan penggunaan nyata, atau perbedaan periode. Selisih itu petunjuk untuk memperbaiki data, bukan bukti kesalahan penagihan. Simpan catatan tanggal agar perbandingan berikutnya dapat diulang."),
            ],
            "example": "Contoh kolom: perangkat | unit | W | jam/hari | hari | kWh perkiraan | sumber angka | catatan mode.",
            "pitfall": "Kesalahan umum: menjumlahkan kWh dari periode yang berbeda lalu membandingkannya dengan satu tagihan bulanan.",
        },
        "en": {
            "title": "A one-sheet home electricity audit",
            "summary": "Build a small record you can improve over time instead of guessing which device caused a bill.",
            "sections": [
                ("Record checkable inputs", "Start with device name, quantity, watts from a label or meter, active hours per day, days used, and where each number came from. Mark figures that are still guesses. You do not need to list every outlet on day one; start with devices used frequently or for long periods."),
                ("Separate estimate types", "For steady loads, calculate watts × hours × days ÷ 1,000. For variable loads, prefer label kWh or a meter reading when available. For standby, record standby hours separately from active hours. Add device estimates only when their periods match."),
                ("Compare with the main meter", "Your sum can differ from the main meter because you missed loads, label ratings differ from real draw, or dates do not match. The gap is a prompt to improve your record, not proof of a billing error. Keep dates so your comparison can be repeated."),
            ],
            "example": "Example columns: device | units | W | hours/day | days | estimated kWh | source of figure | operating-mode note.",
            "pitfall": "Common error: adding kWh from different periods and comparing the sum with one monthly bill.",
        },
        "sources": ["eia", "standby"],
    },
    {
        "slug": "langkah-hemat",
        "id": {
            "title": "Memilih langkah hemat energi berdasarkan data sendiri",
            "summary": "Urutkan perubahan yang dapat diuji, lalu ukur apakah kWh benar-benar berubah.",
            "sections": [
                ("Cari perkiraan terbesar yang masuk akal", "Gabungkan frekuensi penggunaan dan daya, bukan hanya memilih perangkat dengan watt tertinggi. Alat besar yang menyala beberapa menit bisa kalah dari beban sedang yang dipakai sepanjang hari. Mulailah dari nilai yang sumbernya jelas, kemudian ukur yang masih meragukan."),
                ("Ubah satu hal pada satu waktu", "Contoh perubahan sederhana adalah mematikan lampu di ruang kosong atau menjadwalkan perangkat yang memang tidak harus siaga. Catat tanggal perubahan dan bandingkan kWh per hari pada periode yang sebanding. Jika cuaca atau jumlah penghuni berubah, sebutkan perubahan itu saat menilai hasil."),
                ("Jaga kebutuhan utama", "Jangan mengorbankan keselamatan, ventilasi, pencahayaan yang cukup, atau fungsi perangkat penting demi mengejar angka yang lebih kecil. Penghematan terbaik adalah penurunan penggunaan yang terukur dengan kebutuhan rumah tetap terpenuhi. Hasil rumah lain tidak otomatis berlaku pada rumah Anda."),
            ],
            "example": "Contoh: sebelum perubahan 8,0 kWh/hari dan sesudah 7,7 kWh/hari pada kondisi serupa berarti selisih 0,3 kWh/hari; itu observasi, belum bukti tunggal penyebabnya.",
            "pitfall": "Kesalahan umum: mengklaim persentase penghematan pasti hanya dari perubahan spesifikasi perangkat.",
        },
        "en": {
            "title": "Choose energy-saving steps using your own data",
            "summary": "Prioritize changes you can test, then see whether your actual daily kWh changes.",
            "sections": [
                ("Find plausible major uses", "Consider both frequency and power rather than choosing only the appliance with the highest watt rating. A large device used for minutes can use less energy than a moderate load left on all day. Start with figures whose sources are clear, then measure uncertain ones."),
                ("Change one thing at a time", "Simple changes include switching off lights in empty rooms or scheduling a device that does not need standby. Note the change date and compare kWh per day across reasonably similar periods. If weather or occupancy changed, record that when judging the outcome."),
                ("Protect essential needs", "Do not compromise safety, ventilation, adequate light, or an essential device just to reach a lower number. A useful saving is a measured reduction while household needs remain met. Results from another home do not automatically apply to yours."),
            ],
            "example": "Example: 8.0 kWh/day before and 7.7 kWh/day after under similar conditions is a 0.3 kWh/day difference; it is an observation, not proof of a single cause.",
            "pitfall": "Common error: claiming a guaranteed savings percentage from a specification change alone.",
        },
        "sources": ["efficiency", "eia"],
    },
    {
        "slug": "periksa-klaim-hemat",
        "id": {
            "title": "Memeriksa klaim perangkat 'hemat listrik'",
            "summary": "Lima pertanyaan membantu Anda menilai iklan tanpa mengandalkan persentase yang tidak jelas dasarnya.",
            "sections": [
                ("Tanyakan pembandingnya", "Klaim 'lebih hemat 40%' perlu menyebut dibandingkan dengan perangkat apa, pada layanan yang setara, dan dalam pengujian seperti apa. Untuk lampu, cahaya yang dihasilkan perlu sebanding; untuk alat yang bekerja otomatis, kondisi uji dan setelan penting. Persentase tanpa pembanding tidak cukup untuk menghitung tagihan Anda."),
                ("Cari satuan dan periode", "Apakah klaim membahas watt saat aktif, kWh per tahun, biaya energi, atau seluruh biaya kepemilikan? Angka itu menjawab pertanyaan yang berbeda. Jika tersedia label energi resmi, baca konsumsi kWh serta kondisi pengujiannya. Harga dan tarif pada promosi dapat berbeda dari tagihan Anda."),
                ("Hitung ulang dengan masukan sendiri", "Masukkan daya, jam, hari, jumlah unit, dan tarif Anda ke kalkulator perbandingan. Tampilkan selisih kWh terlebih dahulu; biaya hanya perkiraan berdasarkan tarif masukan. Jika data daya nyata tidak ada, tulis bahwa perbandingan bersifat ilustratif dan hindari keputusan mahal hanya dari satu angka."),
            ],
            "example": "Contoh: 'hemat 50%' dari 20 W ke 10 W benar untuk daya saat menyala, tetapi kWh yang dihemat masih bergantung pada jam pemakaian.",
            "pitfall": "Kesalahan umum: membaca persentase pengurangan watt sebagai persentase penurunan seluruh tagihan rumah.",
        },
        "en": {
            "title": "Check an 'energy-saving' product claim",
            "summary": "Ask a few concrete questions before relying on a percentage without a clear baseline.",
            "sections": [
                ("Ask what it is compared with", "A '40% more efficient' claim needs a named comparison product, equivalent service, and test conditions. Lamps should deliver comparable light; automated appliances need comparable settings and conditions. A percentage with no baseline is not enough to predict your bill."),
                ("Find the unit and period", "Does the claim refer to watts while active, kWh per year, energy cost, or total ownership cost? These are different questions. If an official energy label is available, read its kWh and test conditions. The price and electricity rate in an advertisement may differ from yours."),
                ("Recalculate with your inputs", "Enter your watts, hours, days, quantity, and rate in the comparison tool. Look at the kWh difference first; cost is only an estimate based on the rate you enter. If measured power is unavailable, label the comparison as illustrative and avoid an expensive decision based on one number."),
            ],
            "example": "Example: going from 20 W to 10 W is a 50% reduction in power while on, but the kWh saved still depends on operating hours.",
            "pitfall": "Common error: reading a percentage reduction in one device's watts as the same percentage reduction in the entire household bill.",
        },
        "sources": ["aus", "lighting"],
    },
]

SOURCES = {
    "eia": ("U.S. Energy Information Administration — Measuring electricity", "https://www.eia.gov/energyexplained/electricity/measuring-electricity.php"),
    "nist": ("NIST — Conversion factors for energy units", "https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9"),
    "standby": ("U.S. Department of Energy — Measuring standby power", "https://www.energy.gov/cmei/femp/measuring-standby-power"),
    "lighting": ("U.S. Department of Energy — Consumer guide to efficient lighting", "https://www.energy.gov/sites/default/files/2021-08/ES-EE%20Lighting_080921_0.pdf"),
    "aus": ("Australian Government — Energy ratings and running costs", "https://www.energy.gov.au/households/energy-rating"),
    "efficiency": ("U.S. Department of Energy — Why energy efficiency matters", "https://www.energy.gov/energysaver/why-energy-efficiency-matters"),
}
