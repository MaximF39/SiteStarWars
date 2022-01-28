document.querySelector('.paneltop').onclick = function(event) {
  if (event.target.id == 0){
    return;
  }
  for(let i = 1; i <=6; ++i) {
    document.querySelector('.lk'+i).style.display = "none";
  }

  document.querySelector('.'+event.target.id).style.display = "block";
}
//need use addEventListener