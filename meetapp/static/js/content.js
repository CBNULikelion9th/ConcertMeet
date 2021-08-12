(() => {
  const hip_btn = document.querySelector("#hip");
  const bal_btn = document.querySelector("#bal");
  const pop_btn = document.querySelector("#pop");
  const rock_btn = document.querySelector("#rock");
  const jazz_btn = document.querySelector("#jazz");
  const fes_btn = document.querySelector("#fes");
  const indi_btn = document.querySelector("#indi");
  const all_btn = document.querySelector("#all");
  
  const target = document.querySelectorAll(".concert_genre");
  target.forEach((item) => {
    var gen = item.innerText;
    if (gen === "힙합") {
      item.parentNode.classList.add("hiphop");
    } else if (gen === "발라드") {
      item.parentNode.classList.add("ballad");
    } else if (gen === "내한공연") {
      item.parentNode.classList.add("pop");
    } else if (gen === "락"){
      item.parentNode.classList.add("rock");
    } else if (gen === "재즈"){
      item.parentNode.classList.add("jazz");
    } else if (gen === "페스티벌") {
      item.parentNode.classList.add("festival");
    } else if (gen === "인디") {
      item.parentNode.classList.add("indi");
    }
  });

  hip_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll("div.line");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      "div.line.ballad, div.line.pop, div.line.rock, div.line.jazz, div.line.festival, div.line.indi"
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
      "div.line.hiphop, div.line.pop, div.line.rock, div.line.jazz, div.line.festival, div.line.indi"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  pop_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll("div.line");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      "div.line.hiphop, div.line.ballad, div.line.rock, div.line.jazz, div.line.festival, div.line.indi"
      );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  rock_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll("div.line");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      "div.line.hiphop, div.line.ballad, div.line.pop, div.line.jazz, div.line.festival, div.line.indi"
      );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  jazz_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll("div.line");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      "div.line.hiphop, div.line.ballad, div.line.pop, div.line.rock, div.line.festival, div.line.indi"
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
    const target = document.querySelectorAll(
      "div.line.hiphop, div.line.ballad, div.line.pop, div.line.rock, div.line.jazz, div.line.indi"
      );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  indi_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll("div.line");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      "div.line.hiphop, div.line.ballad, div.line.pop, div.line.rock, div.line.jazz, div.line.festival"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  all_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll("div.line");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
  })
})();