(() => {
  const hip_btn = document.querySelector("#hip");
  const bal_btn = document.querySelector("#bal");
  const fes_btn = document.querySelector("#fes");

  const target = document.querySelectorAll(".concert_genre");
  target.forEach((item) => {
    var gen = item.innerText;
    if (gen === "힙합") {
      item.parentNode.classList.add("hiphop");
    } else if (gen === "인디") {
      item.parentNode.classList.add("indi");
    } else if (gen === "페스티벌") {
      item.parentNode.classList.add("festival");
    }
  });

  hip_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll("div.line");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      "div.line.indi, div.line.festival"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  bal_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll("div.line");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      "div.line.hiphop, div.line.festival"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  fes_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll("div.line");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll("div.line.hiphop, div.line.indi");
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });
})();
