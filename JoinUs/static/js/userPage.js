/* 닉네임 중복체크! */
function changeNickname() {
  let changenickname = ""
  changenickname = prompt('변경할 닉네임을 적어주세요', '')
  if (changenickname == '') {
    alert('닉네임을 입력해주세요')
    return;
  }

  $.ajax({
    url: '/member/updateNickname?user_nickname=' + changenickname,
    type: 'get',
    dataType: 'json',
    success: function (response) {
      if (response.result != 'success') {
        console.error(response.data)
        return;
      }
      if (response.data == 'exist') {
        alert("존재하는 닉네임 입니다!ㅇㅠㅇ");

        return;
      } else {
        alert("닉네임이 변경되었습니다.")
        window.location.reload()
        //$('#user-nickname').text("회원 닉네임 : " + changenickname)
        return;
      }
    },
    error: function (xhr, error) {
      alert("서버와의 통신에서 문제가 발생했습니다.");
      console.error("error : " + error);
    }
  })

}

function deleteUser() {
  let deletcheck = confirm("정말로 회원 탈퇴를 하실 겁니까?")
  if (deletcheck) {
    alert("비밀번호를 입력해 주세요")
    $('#checkpw').css("display", 'block')
  }
}

