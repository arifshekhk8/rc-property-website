"use strict";

const guide = document.querySelector("#guide-dialog");
document.querySelectorAll("[data-open-guide]").forEach((button) => {
  button.addEventListener("click", () => guide.showModal());
});
document.querySelectorAll("dialog").forEach((dialog) => {
  dialog.addEventListener("click", (event) => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (
      event.clientX < bounds.left ||
      event.clientX > bounds.right ||
      event.clientY < bounds.top ||
      event.clientY > bounds.bottom
    )
      dialog.close();
  });
});

const photos = [...document.querySelectorAll("[data-lightbox]")];
const photoDialog = document.querySelector("#photo-dialog");
let photoIndex = 0;
function displayPhoto(index) {
  photoIndex = (index + photos.length) % photos.length;
  const item = photos[photoIndex];
  const img = document.querySelector("#photo-image");
  img.src = item.dataset.src;
  img.alt = item.querySelector("img").alt;
  document.querySelector("#photo-caption").textContent = item.dataset.caption;
}
photos.forEach((button, index) =>
  button.addEventListener("click", () => {
    displayPhoto(index);
    photoDialog.showModal();
  }),
);
document
  .querySelector("[data-photo-prev]")
  ?.addEventListener("click", () => displayPhoto(photoIndex - 1));
document
  .querySelector("[data-photo-next]")
  ?.addEventListener("click", () => displayPhoto(photoIndex + 1));
photoDialog?.addEventListener("keydown", (event) => {
  if (event.key === "ArrowLeft") {
    event.preventDefault();
    displayPhoto(photoIndex - 1);
  }
  if (event.key === "ArrowRight") {
    event.preventDefault();
    displayPhoto(photoIndex + 1);
  }
});

const panoramaButton = document.querySelector("#load-panorama");
panoramaButton?.addEventListener("click", () => {
  panoramaButton.disabled = true;
  const container = document.querySelector("#panorama");
  const script = document.createElement("script");
  script.src = container.dataset.panoramaJs;
  function failed() {
    const message = document.createElement("p");
    message.className = "media-error";
    message.setAttribute("role", "status");
    message.textContent = container.dataset.error;
    container.replaceChildren(message);
  }
  script.addEventListener("load", () => {
    try {
      container.replaceChildren();
      const viewer = window.pannellum.viewer("panorama", {
        type: "equirectangular",
        panorama: container.dataset.panoramaUrl,
        autoLoad: true,
        autoRotate: 0,
        escapeHTML: true,
        mouseZoom: false,
        showFullscreenCtrl: true,
        showControls: true,
      });
      viewer.on("error", failed);
    } catch {
      failed();
    }
  });
  script.addEventListener("error", failed);
  document.head.append(script);
});

document.querySelector("[data-error-summary]")?.focus();
document.querySelectorAll("[data-inquiry-form]").forEach((form) => {
  form.addEventListener("submit", () => {
    const button = form.querySelector("button[type=submit]");
    button.disabled = true;
    button.textContent = button.dataset.sendingLabel;
  });
});
window.addEventListener("pageshow", () =>
  document.querySelectorAll("[data-submit-label]").forEach((button) => {
    button.disabled = false;
    button.textContent = button.dataset.submitLabel;
  }),
);
