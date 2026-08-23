(function () {
  "use strict";

  var body = document.body;
  var toggle = document.querySelector(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".nav-links a").forEach(function (link) {
    link.addEventListener("click", function () {
      body.classList.remove("nav-open");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
    });
  });

  document.querySelectorAll("form[data-whatsapp]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var name = (form.querySelector("[name=name]") || {}).value || "";
      var phone = (form.querySelector("[name=phone]") || {}).value || "";
      var service = (form.querySelector("[name=service]") || {}).value || "";
      var district = (form.querySelector("[name=district]") || {}).value || "";
      var message = (form.querySelector("[name=message]") || {}).value || "";
      var text =
        "Merhaba, ben " + name +
        ".\nTelefon: " + phone +
        "\nHizmet: " + service +
        (district ? "\nBölge: " + district : "") +
        "\nMesaj: " + message +
        "\nFiyat teklifi almak istiyorum.";
      window.open("https://wa.me/905446304003?text=" + encodeURIComponent(text), "_blank", "noopener");
    });
  });

  if (typeof gtag === "function") {
    document.querySelectorAll('a[href^="https://wa.me"]').forEach(function (link) {
      link.addEventListener("click", function () {
        gtag("event", "conversion", { send_to: "AW-17270904841" });
      });
    });
  }
})();
