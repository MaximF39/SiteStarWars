// function showpass(id) {
//     element = document.getElementById(id);
//     if (element.type === "password") {
//       element.type = "text";
//     } else {
//       element.type = "password";
//     }
//   }

document.querySelector('.paneltop').onclick = function(event) {
  for(let i = 1; i <=6; ++i) {
    document.querySelector('.lk'+i).style.display = "none";
  }

  document.querySelector('.'+event.target.id).style.display = "block";
}