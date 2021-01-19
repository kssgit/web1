/* 중복체크! */



$(function () {
  $('#btn-email').click(function () {
    var email = $('#user-email').val()
    if (email == '') {
      alert('이메일을 입력해주세요.')
      return;
    }
    let email_pat = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
    if (!email_pat.test(email)) {
      alert("이메일 형식에 맞게 쓰세요!!")
      return;
    }
    $.ajax({
      url: '../member/emailCheck?user_email=' + email,
      type: 'get',
      dataType: 'json',
      success: function (response) {
        if (response.result != 'success') {
          console.error(response.data)
          return;
        }
        if (response.data == 'exist') {
          alert("존재하는 이메일 입니다!ㅇㅠㅇ");
          $('#user-email').val('').focus();
          return;
        } else {
          alert("사용할 수 있는 E-mail 입니다")
          $('#btn-email').hide();
          $("#btn-email").attr("email_check_result", "success");
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


$(function () {
  $('#btn-nickname').click(function () {
    var nickname = $('#user-nickname').val()
    if (nickname == '') {
      alert('닉네임을 입력해주세요')
      return;
    }

    $.ajax({
      url: '../member/nicknameCheck?user_nickname=' + nickname,
      type: 'get',
      dataType: 'json',
      success: function (response) {
        if (response.result != 'success') {
          console.error(response.data)
          return;
        }
        if (response.data == 'exist') {
          alert("존재하는 닉네임 입니다!ㅇㅠㅇ");
          $('#user-nickname').val('').focus();
          return;
        } else {
          alert("사용할 수 있는 닉네임 입니다")
          $('#btn-nickname').hide();
          $("#btn-nickname").attr("nickname_check_result", "success");
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
$('#user-email').change(function () {

  $('#btn-email').show();
  $("#btn-email").attr("email_check_result", "fail");


});

$('#user-nickname').change(function () {

  $('#btn-nickname').show();
  $("#btn-nickname").attr("nickname_check_result", "fail");

});


$('#join-form').submit(function () {

  if ($("#btn-email").attr("email_check_result") == "fail") {
    alert("이메일 중복체크를 해주시기 바랍니다.");
    $("#user-email").focus();
    return false;
  }
  if ($("#btn-nickname").attr("nickname_check_result") == "fail") {
    alert("닉네임 중복체크를 해주시기 바랍니다.");
    $("#user-nickname").focus();
    return false;
  }
});