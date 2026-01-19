from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 사용자 데이터를 저장할 딕셔너리
user_data = {}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('user_message')  # 사용자가 보낸 메시지
    
    # 서비스 종류 선택 후
    if '서비스 종류' not in user_data:
        if user_message == "서비스_랜딩페이지":
            user_data['서비스 종류'] = "랜딩 페이지"
        elif user_message == "서비스_기업홈페이지":
            user_data['서비스 종류'] = "기업 홈페이지"
        elif user_message == "서비스_모바일앱":
            user_data['서비스 종류'] = "모바일 앱"
        elif user_message == "서비스_쇼핑몰":
            user_data['서비스 종류'] = "쇼핑몰"
        return jsonify({
            "text": "예산 구간을 선택해주세요.",
            "buttons": [
                {"text": "~100만원", "action": "예산_100만원이하"},
                {"text": "100~300만원", "action": "예산_100_300만원"},
                {"text": "300~700만원", "action": "예산_300_700만원"},
                {"text": "700만원 이상", "action": "예산_700만원이상"}
            ]
        })
    
    # 예산 구간 설정 후
    if '예산' not in user_data:
        if user_message == "~100만원":
            user_data['예산'] = "~100만원"
        elif user_message == "100~300만원":
            user_data['예산'] = "100~300만원"
        elif user_message == "300~700만원":
            user_data['예산'] = "300~700만원"
        elif user_message == "700만원 이상":
            user_data['예산'] = "700만원 이상"
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
    
    # 업종 선택 후 자동으로 요약 텍스트 보여주기
    if '업종' not in user_data:
        if user_message == "업종_요식업":
            user_data['업종'] = "요식업"
        elif user_message == "업종_교육학원":
            user_data['업종'] = "교육/학원"
        elif user_message == "업종_병원의료":
            user_data['업종'] = "병원/의료"
        elif user_message == "업종_패션뷰티":
            user_data['업종'] = "패션/뷰티"
        elif user_message == "업종_IT스타트업":
            user_data['업종'] = "IT/스타트업"
        elif user_message == "업종_기타":
            user_data['업종'] = "기타"
        
        # 사용자가 '요약'이라고 입력한 경우, 저장된 정보를 요약하여 출력
        if user_message.lower() == "요약":
            summary_text = f"""
            당신의 선택은:
            서비스 종류: {user_data['서비스 종류']}
            예산: {user_data['예산']}
            업종: {user_data['업종']}
            """
            return jsonify({
                "text": summary_text,
                "buttons": [{"text": "다시 시작하기", "action": "시작하기"}]
            })
        
        return jsonify({
            "text": "당신의 선택을 요약해 드리겠습니다.",
            "buttons": [{"text": "다시 시작하기", "action": "시작하기"}]
        })

    return jsonify({"text": "계속 진행하려면 선택해주세요."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
