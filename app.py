from flask import Flask
import os
app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MAN 1 Cirebon</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}
.top{display:flex;align-items:center;gap:10px;padding:14px 20px;background:#fff;box-shadow:0 2px 8px #0001;position:sticky;top:0;z-index:10}
.top b{color:#1e2a4a}.lg{font-size:22px}
.menu-btn{margin:12px 20px;border:1px solid #ddd;background:#fff;padding:7px 14px;font-size:22px;border-radius:6px}
#nav{display:none;background:#fff;padding:10px 20px;border-top:1px solid #eee}
#nav a{display:block;padding:12px 0;text-decoration:none;color:#222;font-weight:700;font-size:14px;border-bottom:1px solid #f5f5f5}
#nav a.y{color:#feb500}
.sub{display:none;background:#f3f4f5;margin:6px 0;padding:8px 12px;border-radius:6px}
.sub a{font-weight:400!important;font-size:13px;padding:7px 0!important;border:none!important}
.hero{height:320px;background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,.55)),url('https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=800');background-size:cover;background-position:center;display:flex;align-items:center;justify-content:center;color:#fff;text-align:center;position:relative}
.arr{position:absolute;top:50%;transform:translateY(-50%);background:#feb500;border:none;color:#fff;width:38px;height:38px;font-size:22px;border-radius:4px}
.l{left:12px}.r{right:12px}
.btns{margin-top:16px;display:flex;gap:10px;justify-content:center}
.btns button{padding:10px 20px;border:none;font-weight:700;border-radius:3px}
.yb{background:#feb500;color:#fff}.wb{background:#fff;color:#222}
.stats{padding:0 20px}
.stat{display:flex;gap:16px;align-items:center;padding:20px 0;border-bottom:1px solid #eee}
.ic{width:48px;height:48px;background:#feb500;color:#fff;display:flex;align-items:center;justify-content:center;font-size:20px}
.about{padding:22px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.grid img{width:100%;height:140px;object-fit:cover;border-radius:4px}
.kecil{color:#feb500;font-size:11px;font-weight:800;margin-top:18px;letter-spacing:1px}
.btnk{background:#feb500;color:#fff;border:none;padding:13px;width:100%;font-weight:800;margin-top:12px;border-radius:3px}
</style></head><body>
<div class="top"><span class="lg">🏫</span><b>MAN 1 CIREBON</b></div>
<button class="menu-btn" onclick="document.getElementById('nav').style.display=document.getElementById('nav').style.display=='block'?'none':'block'">☰</button>
<div id="nav">
<a class="y">HOME</a>
<a onclick="document.getElementById('p1').style.display=document.getElementById('p1').style.display=='block'?'none':'block'">PROFILE ▼</a>
<div id="p1" class="sub"><a>Profile Madrasah</a><a>Kepala Madrasah dan Wakil</a><a>Guru Pengajar</a><a>Staff Tata Usaha</a><a>Pengasuh Santri Tahfidz</a><a>Keamanan dan K3</a><a>Purna Bhakti</a><a>Komite Madrasah</a></div>
<a onclick="document.getElementById('p2').style.display=document.getElementById('p2').style.display=='block'?'none':'block'">KURIKULUM ▼</a>
<div id="p2" class="sub"><a>E-Learning</a><a>RDM Raport</a><a>E-Kinerja</a><a>CBT Online</a></div>
<a onclick="document.getElementById('p3').style.display=document.getElementById('p3').style.display=='block'?'none':'block'">KESISWAAN ▼</a>
<div id="p3" class="sub"><a>SIPS</a><a>Pemilihan Ketua Osis Online</a></div>
<a>PTSP</a><a>GALERI</a><a>BERITA</a><a>CONTACT</a>
</div>
<div class="hero">
<button class="arr l">‹</button>
<div><h1>MAN 1 CIREBON</h1><div class="btns"><button class="yb">PPDB</button><button class="wb">PROFILE</button></div></div>
<button class="arr r">›</button>
</div>
<div class="stats">
<div class="stat"><div class="ic">👤</div><div><div style="font-size:13px;color:#666">Jumlah Siswa</div><b style="font-size:20px">1255</b></div></div>
<div class="stat"><div class="ic">👥</div><div><div style="font-size:13px;color:#666">Jumlah Guru</div><b style="font-size:20px">75</b></div></div>
<div class="stat"><div class="ic">📄</div><div><div style="font-size:13px;color:#666">Jumlah Pegawai</div><b style="font-size:20px">20</b></div></div>
</div>
<div class="about">
<div class="grid"><img src="https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=400"><img src="https://images.unsplash.com/photo-1562774053-701939374585?w=400" style="margin-top:18px"></div>
<div class="kecil">TENTANG KAMI</div>
<h2 style="margin:8px 0;line-height:1.2">Selamat Datang di<br>MAN 1 Cirebon</h2>
<p style="font-size:13px;color:#888">website sekolah MAN 1 Cirebon - tanpa nomor telepon sesuai request</p>
<button class="btnk">Baca Selengkapnya</button>
</div>
</body></html>
"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
