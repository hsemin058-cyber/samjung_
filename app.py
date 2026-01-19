from flask import Flask, request, jsonify

app = Flask(__name__)

# 사용자 데이터를 저장할 딕셔너리
user_data = {}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('user_message')  # 사용자가 보낸 메시지
    
    # 각 질문에 대한 버튼 선택 및 처리
    if '서비스 종류' not in user_data:
        return jsonify({
            "text": "원하는 서비스 종류를 선택해주세요.",
            "buttons": [
                {"text": "랜딩 페이지", "action": "서비스_랜딩페이지"},
                {"text": "기업 홈페이지", "action": "서비스_기업홈페이지"},
                {"text": "모바일 앱", "action": "서비스_모바일앱"},
                {"text": "쇼핑몰", "action": "서비스_쇼핑몰"}
            ]
        })
    
    # 예산 구간 설정
    if user_message == "서비스_랜딩페이지":
        user_data['서비스 종류'] = "랜딩 페이지"
        return jsonify({
            "text": "예산 구간을 선택해주세요.",
            "buttons": [
                {"text": "~100만원", "action": "예산_100만원이하"},
                {"text": "100~300만원", "action": "예산_100_300만원"},
                {"text": "300~700만원", "action": "예산_300_700만원"},
                {"text": "700만원 이상", "action": "예산_700만원이상"}
            ]
        })

    # 예산 구간 설정 후 업종 선택
    if user_message == "예산_100만원이하":
        user_data['예산'] = "~100만원"
        return jsonify({
            "text": "업종을 선택해주세요.",
            "buttons": [
                {"text": "요식업", "action": "업종_요식업"},
                {"text": "교육/학원", "action": "업종_교육학원"},
                {"text": "병원/의료", "action": "업종_병원의료"},
                {"text": "패션/뷰티", "action": "업종_패션뷰티"},
                {"text": "IT/스타트업", "action": "업종_IT스타트업"},
                {"text": "기타", "action": "업종_기타"}
            ]
        })
    
    # 최종 요약: 업종 선택 후
    if user_message == "업종_요식업":
        user_data['업종'] = "요식업"
        return jsonify({
            "text": f"당신의 선택은: 서비스 종류 - {user_data['서비스 종류']}, 예산 - {user_data['예산']}, 업종 - {user_data['업종']}",
            "buttons": [{"text": "다시 시작하기", "action": "시작하기"}]
        })

    return jsonify({"text": "계속 진행하려면 선택해주세요."})

if __name__ == "__main__":
    app.run(debug=True)
