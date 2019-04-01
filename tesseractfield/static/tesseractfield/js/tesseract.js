var TESERACT_URL = '/api/tesseract/';

function tesseract(field, file) {
  var textarea = document.getElementsByName(field)[0];
  textarea.value = 'loading...';

  var fd = new FormData();
  fd.append("file", file);

  var xhr = new XMLHttpRequest();
  xhr.open("POST", TESERACT_URL);
  xhr.setRequestHeader("X-CSRFToken", document.getElementsByName("csrfmiddlewaretoken")[0].value);
  xhr.setRequestHeader("enctype", "multipart/form-data");
  xhr.onload = function(event) {
    if (xhr.status == 200) {
      var data = JSON.parse(xhr.response);
      textarea.value = data['transcript'];
    } else {
      console.log("Error " + xhr.status + " occurred when trying to upload your file.");
    }
  };
  xhr.send(fd);
}
