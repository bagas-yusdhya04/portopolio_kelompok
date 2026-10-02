function kirimWhatsApp() {

    const nama = document.getElementById("nama").value;
    const jasa = document.getElementById("jasa").value;
    const deskripsi = document.getElementById("deskripsi").value;

    if (nama === "" || deskripsi === "") {
        alert("Silakan lengkapi data terlebih dahulu.");
        return;
    }

    const nomor = "6281234567890";

    const pesan =
        "Halo KreasiDigital!%0A%0A" +
        "Nama: " + nama + "%0A" +
        "Jasa: " + jasa + "%0A" +
        "Kebutuhan: " + deskripsi;

    const url =
        "https://wa.me/" + nomor + "?text=" + pesan;

    window.open(url, "_blank");
}