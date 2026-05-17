import test from "node:test";
import assert from "node:assert/strict";
import { parseReportDetail, parseSearchResults, summarizeSeismicChart } from "../src/parser.js";

const IJEN_HTML = `
<title>Laporan Aktivitas Gunung Api - Ijen, Sabtu - 16 Mei 2026, periode 00:00-24:00 WIB</title>
<h5><span class="badge badge-success">Level I (Normal)</span></h5>
<h5 class="card-title tx-dark tx-medium mg-b-10">Ijen, Sabtu - 16 Mei 2026, periode 00:00-24:00 WIB</h5>
<p class="card-subtitle tx-normal mg-b-15">Dibuat oleh,  Ahmad Subhan Nur Fajidi, A.Md.</p>
<p class="col-lg-6 pd-0">Gunung Api Ijen terletak di Kab\\Kota Banyuwangi, Bondowoso, Jawa Timur dengan posisi geografis di Latitude -8.058&deg;LU, Longitude 114.242&deg;BT dan memiliki ketinggian 2386 mdpl</p>
<img class="img-fluid" src="https://magma.vsi.esdm.go.id/img/ga/IJE/IJE202605162400.png" alt="Ijen">
<script>var query = "MAG_CODE='IJE'"; data: {id: '315786'}</script>
<h6 class="slim-card-title">Pengamatan Visual</h6><p>Gunung api terlihat jelas. Teramati asap kawah utama berwarna putih.</p>
<h6 class="slim-card-title">Keterangan Lainnya</h6><p>-Waspadai potensi gas berbahaya</p>
<h6 class="slim-card-title">Klimatologi</h6><p>Cuaca berawan hingga hujan.</p>
<h6 class="slim-card-title">Pengamatan Kegempaan</h6>
<p>2 kali gempa Vulkanik Dangkal dengan amplitudo 3-4 mm.</p><hr>
<p>1 kali gempa Tremor Menerus dengan amplitudo 0.5-2 mm.</p><hr>
</div></div></div>
<h6 class="slim-card-title">Rekomendasi</h6>
<p>1) Masyarakat dan pengunjung/wisatawan tidak turun dan mendekati dasar Kawah G. Ijen.<br />2) Tidak bermalam radius 500 m.</p>`;

test("parseReportDetail normalizes MAGMA detail HTML", () => {
  const report = parseReportDetail(
    IJEN_HTML,
    "https://magma.esdm.go.id/v1/gunung-api/laporan/315786?signature=test"
  );

  assert.equal(report.reportId, "315786");
  assert.equal(report.volcanoCode, "IJE");
  assert.equal(report.name, "Ijen");
  assert.equal(report.statusLevel, "Level I (Normal)");
  assert.equal(report.lat, -8.058);
  assert.equal(report.lon, 114.242);
  assert.equal(report.elevation, 2386);
  assert.equal(report.seismic.length, 2);
  assert.equal(report.recommendations.length, 2);
});

test("parseSearchResults extracts latest report links", () => {
  const html = `
  <div class="timeline-item">
    <div class="timeline-time"><small>Periode 00:00-24:00 WIB</small></div>
    <div class="timeline-body">
      <p class="timeline-title"><a href="#">Bromo</a><span class="badge badge-warning tx-white">Level II (Waspada)</span></p>
      <p class="timeline-author">Dibuat oleh <span class="tx-primary">Budi Marwanto</span> - Sabtu, 16 Mei 2026</p>
      <p>Gunung api terlihat jelas.</p>
      <a href="https://magma.esdm.go.id/v1/gunung-api/laporan/315742?signature=abc" class="card-link">Lihat Detail</a>
    </div>
  </div>`;

  const [item] = parseSearchResults(html);
  assert.equal(item.name, "Bromo");
  assert.equal(item.statusLevel, "Level II (Waspada)");
  assert.equal(item.reportId, "315742");
});

test("summarizeSeismicChart totals each series", () => {
  const summary = summarizeSeismicChart({
    categories: ["2026-05-15", "2026-05-16"],
    series: [{ name: "Tektonik Jauh", data: [1, 3], color: "#fff" }]
  });

  assert.equal(summary.lastDate, "2026-05-16");
  assert.equal(summary.series[0].total90, 4);
  assert.equal(summary.series[0].latest, 3);
});
