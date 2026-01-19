use warp::Filter;
use serde::{Serialize, Deserialize};
use tokio;
use std::env;

#[derive(Serialize, Deserialize)]
struct Response {
    message: String,
}

#[tokio::main]
async fn main() {
    // 환경 변수에서 PORT 값을 가져옵니다. 없으면 기본값 3030 사용
    let port = env::var("PORT").unwrap_or_else(|_| "3030".to_string());
    
    // 라우팅 설정: "/hello"로 들어오는 요청에 대해 JSON 응답 반환
    let hello = warp::path("hello")
        .map(|| warp::reply::json(&Response {
            message: String::from("Hello, world!"),
        }));

    // 서버 시작: 0.0.0.0 주소로 포트를 환경변수에서 가져와 바인딩
    warp::serve(hello)
        .run(([0, 0, 0, 0], port.parse().unwrap()))  // 모든 IP에서 바인딩
        .await;
}
