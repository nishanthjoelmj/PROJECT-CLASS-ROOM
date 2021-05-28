$(document).ready(function () {
  $("#video").change(function () {
    call();
  });
});

const file_vd = document.getElementById("video");
const progress_bar = document.getElementsByClassName("progress-bar-filler")[0];

const progress_text = document.getElementsByClassName("progress-bar-text")[0];

function submitVDFORM(e) {
  e.preventDefault();
  let vdform = document.getElementById("videoform");
  var token = $("input[name=csrfmiddlewaretoken]").val();
  let caption = document.getElementById("id_captions").value;
  let vd_file = document.getElementById("video");
  let eventsname = document.getElementById("E").value;
  let formsdata = new FormData();
  formsdata.append("csrfmiddlewaretoken", token);
  formsdata.append("captions", caption);
  formsdata.append("video", vd_file.files[0]);
  formsdata.append("events",eventsname);

  formTask = $.ajax({
    xhr: function () {
      var xhr = new window.XMLHttpRequest();
      xhr.upload.addEventListener(
        "progress",
        function (evt) {
          let percentComplete = 0;
          if (evt.lengthComputable) {
            percentComplete = (evt.loaded / evt.total) * 100;

          } else percentComplete = 0;

          progress_bar.style.width = percentComplete.toFixed(2) + "%";
          progress_text.textContent = percentComplete.toFixed(1) + "%";
        },
        false
      );
      return xhr;
    },

    type: "POST",
    url: "/upload/ajax",

    //contentType: 'multipart/form-data',

    enctype: "multipart/form-data",
    data: formsdata,
    success: function (respone) {
      alert(" FILE UPLOADED ");
       vdform.reset();
         percentComplete = 0;
        progress_bar.style.width = percentComplete.toFixed(2) + "%";
        progress_text.textContent = percentComplete.toFixed(1) + "%";

    },
    error: function (error) {
      alert(error.responseJSON.video);
    },

    cache: false,
    contentType: false,
    processData: false,
  });

  return false;
}