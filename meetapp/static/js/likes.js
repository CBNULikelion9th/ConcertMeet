// const button = document.querySelector('.btn') //클래스를 만족하는 첫 번째 요소 검색해서 변수에 담음
// button.addEventListener('click', () => {
//     button.classList.toggle('liked') //기존 값이 0이었다면 1로 바뀌고 기존 값이 1이었다면, 0으로 바뀌게 됨.
// //toggle 메서드는 클래스가 존재한다면 클래스를 제거하고, 클래스가 존재하지 않는다면 클래스를 추가하는 메서드.
// })
(() => {
  const button = document.querySelectorAll(".btn-icon"); //클래스를 만족하는 첫 번째 요소 검색해서 변수에 담음

  button.forEach(function (item) {
    item.addEventListener("click", () => {
      item.classList.toggle("likes");
    });
  });

  // button.addEventListener("click", () => {
  //   button.classList.toggle("likes"); //기존 값이 0이었다면 1로 바뀌고 기존 값이 1이었다면, 0으로 바뀌게 됨.
  //   //toggle 메서드는 클래스가 존재한다면 클래스를 제거하고, 클래스가 존재하지 않는다면 클래스를 추가하는 메서드.
  // });
})();
