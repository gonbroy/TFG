function getBusqueda() {
  return JSON.parse(localStorage.getItem("busquedaVuelo") || "null");
}

function setBusqueda(datos) {
  localStorage.setItem("busquedaVuelo", JSON.stringify(datos));
}

function clearBusqueda() {
  localStorage.removeItem("busquedaVuelo");
}