  (async function () {

    async function load(id, file){
      const el = document.getElementById(id);
      if (!el) return; // si no existe en la página, no pasa nada

      try {
        const res = await fetch(file, { cache: "no-store" });
        if (!res.ok) throw new Error(`${file} (HTTP ${res.status})`);

        const html = await res.text();
        el.innerHTML = html;

        console.log(`${id} cargado correctamente ✅`);

      } catch (err) {
        console.error(`Error cargando ${id}:`, err);
        el.innerHTML = `<!-- Error cargando ${id} -->`;
      }
    }

    // Cargar header y footer (misma carpeta html)
    await load("header", "./header.html");
    await load("footer", "./footer.html");

    // Año automático si existe
    const year = document.getElementById("year");
    if (year) year.textContent = new Date().getFullYear();

  })();