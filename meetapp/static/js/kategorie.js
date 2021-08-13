(()=> {
  const hip_btn = document.querySelector("#hip");
  const bal_btn = document.querySelector("#bal");
  const pop_btn = document.querySelector("#pop");
  const rock_btn = document.querySelector("#rock");
  const jazz_btn = document.querySelector("#jazz");
  const fes_btn = document.querySelector("#fes");
  const indi_btn = document.querySelector("#indi");
  const all_btn = document.querySelector("#all");

  const target = document.querySelectorAll(".post");
  target.forEach((item) => {
    var gen = item.querySelector(".category");
    if (gen.innerText === "#힙합") {
      item.classList.add("hiphop");
    } else if (gen.innerText === "#발라드") {
      item.classList.add("ballad");
    } else if (gen.innerText === "#팝") { // == 내한공연
      item.classList.add("pop");
    } else if (gen.innerText === "#락"){
      item.classList.add("rock");
    } else if (gen.innerText === "#재즈"){
      item.classList.add("jazz");
    } else if (gen.innerText === "#페스티벌") {
      item.classList.add("festival");
    } else if (gen.innerText === "#인디") {
      item.classList.add("indi");
    } else {
      item.classList.add("all");
    }
  });

  hip_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll(".post");
    console.log(clear);
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      ".ballad, .pop, .rock, .jazz, .festival, .indi, .all"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  bal_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll(".post");
    console.log(clear);
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      ".hiphop, .pop, .rock, .jazz, .festival, .indi, .all"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  pop_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll(".post");
    console.log(clear);
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      ".hiphop, .ballad, .rock, .jazz, .festival, .indi, .all"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  rock_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll(".post");
    console.log(clear);
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      ".hiphop, .ballad, .pop, .jazz, .festival, .indi, .all"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  jazz_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll(".post");
    console.log(clear);
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      ".hiphop, .ballad, .pop, .rock, .festival, .indi, .all"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  fes_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll(".post");
    console.log(clear);
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      ".hiphop, .ballad, .pop, .rock, .jazz, .indi, .all"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  indi_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll(".post");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
    const target = document.querySelectorAll(
      ".hiphop, .ballad, .pop, .rock, .jazz, .festival, .all"
    );
    target.forEach((item) => {
      item.classList.toggle("hide");
    });
  });

  all_btn.addEventListener("click", () => {
    const clear = document.querySelectorAll(".post");
    clear.forEach((item) => {
      item.classList.remove("hide");
    });
  })
})();