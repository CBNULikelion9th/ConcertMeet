const hip_btn = document.querySelector("#hip");
const bal_btn = document.querySelector(".bal");

function separate_genre() {
  const target = document.querySelectorAll(".concert_genre");
  target.forEach((item) => {
    var gen = item.innerText;
    if (gen === "힙합") {
      item.parentNode.classList.add("hiphop");
    } else if (gen === "인디") {
      item.parentNode.classList.add("indi");
    }
  });
}

hip_btn.addEventListener("click", () => {
  const clear = document.querySelectorAll("div.line");
  clear.forEach((item) => {
    item.classList.remove("hide");
  });
  const target = document.querySelectorAll("div.line.indi");
  target.forEach((item) => {
    item.classList.toggle("hide");
  });
});

bal_btn.addEventListener("click", () => {
  const clear = document.querySelectorAll("div.line");
  clear.forEach((item) => {
    item.classList.remove("hide");
  });
  const target = document.querySelectorAll("div.line.hiphop");
  target.forEach((item) => {
    item.classList.toggle("hide");
  });
});

separate_genre();
