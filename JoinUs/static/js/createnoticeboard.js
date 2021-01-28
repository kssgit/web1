$(document).ready(function () {
  var fileTarget = $('.filebox .upload-hidden');

  fileTarget.on('change', function () {
    if (window.FileReader) {
      // 파일명 추출
      var filename = $(this)[0].files[0].name;
    }

    else {
      // Old IE 파일명 추출
      var filename = $(this).val().split('/').pop().split('\\').pop();
    };

    $(this).siblings('.upload-name').val(filename);
  });

  //preview image 
  var imgTarget = $('.preview-image .upload-hidden');

  imgTarget.on('change', function () {
    var parent = $(this).parent();
    parent.children('.upload-display').remove();

    if (window.FileReader) {
      //image 파일만
      if (!$(this)[0].files[0].type.match(/image\//)) return;

      var reader = new FileReader();
      reader.onload = function (e) {
        var src = e.target.result;
        parent.prepend('<div class="upload-display"><div class="upload-thumb-wrap"><img src="' + src + '" class="upload-thumb"></div></div>');
      }
      reader.readAsDataURL($(this)[0].files[0]);
    }

    else {
      $(this)[0].select();
      $(this)[0].blur();
      var imgSrc = document.selection.createRange().text;
      parent.prepend('<div class="upload-display"><div class="upload-thumb-wrap"><img class="upload-thumb"></div></div>');

      var img = $(this).siblings('.upload-display').find('img');
      img[0].style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(enable='true',sizingMethod='scale',src=\"" + imgSrc + "\")";
    }
  });
});


//submit 체크 

$('#join-form').submit(function () {
  //이미지 업로드 여부 확인
  if (!$('#input-file').val()) {
    alert('대표 이미지를 첨부해주세요~');

    return false;
  }

  let check = $("input:radio[name='m_category']").is(":checked");
  if (!check) {
    alert("카테고리를 체크해주세요");

    return false;
  }

  if ($("#btn-name").attr("name_check_result") == "fail") {
    alert("중복 체크해주세요")
    return false;
  }

  let checkurl = /(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;
  let m_url = document.getElementById('m-url').value;
  if (!checkurl.test(m_url)) {
    alert('올바른 url을 적어주세요');
    return false;
  }


});

// 모임 이름 중복 체크 

$(function () {
  $('#btn-name').click(function () {
    let name = $('#m-name').val()
    if (name == '') {
      alert('모임 이름을 입력해주세요.')
      return false;
    }

    $.ajax({
      url: '/notice/meetnameCheck?m_name=' + name,//.을 붙이는 것과 안붙이는 것의 차이?
      type: 'get',
      dataType: 'json',
      success: function (response) {
        if (response.result != 'success') {
          console.error(response.data)
          return;
        }
        if (response.data == 'exist') {
          alert("존재하는 이름 입니다!ㅇㅠㅇ");
          $('#m-name').val('').focus();
          return;
        } else {
          alert("사용할 수 있는 이름 입니다")
          $('#btn-name').hide();
          $("#btn-name").attr("name_check_result", "success");
          return;
        }
      },
      error: function (xhr, error) {
        alert("서버와의 통신에서 문제가 발생했습니다.");
        console.error("error : " + error);
      }
    })
  })
});


// 중복 체크후 데이타 수정 한 경우 
$('#m-name').change(function () {

  $('#btn-name').show();
  $("#btn-name").attr("name_check_result", "fail");
  $("#btn-name").focus();

});


