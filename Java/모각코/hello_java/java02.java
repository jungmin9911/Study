package hello_java;

public class java02 {

	public static void main(String[] args) {
		/*
		메소드(Method) - 함수와 같은 기능을 하지만 메소드는 클래스 안의 함수를 부르는 명칭 (클래스에서 사용할 수 있는 기능)
		System.out.println("...")
		=> System이라는 클래스 안에 out이라는 변수 안에 println이라는 메소드
		*/
		
		//출력 메소드 - print, printf, println
		//print : 줄바꿈 없이 출력(줄바꿈 하려면 '\n' 입력
		System.out.print("안녕하세요");
		System.out.print("코뮤니티입니다");
		System.out.print("모각코 좋아요\n");
		
		//println : 문장 출력 후 자동 줄바꿈
		System.out.print("\n");
		System.out.println("안녕하세요");
		System.out.println("코뮤니티입니다");
		System.out.println("모각코 좋아요");
		
		//printf : 지시자를 이용해 값을 변환하여 출력 가능
		/*
		지시자
		%d : 정수(decimal) 형식으로 출력 / %f : 실수(floating-point) 형식으로 출력
		%c : 문자(character) 형식으로 출력 / %s : 문자열(string) 형식으로 출력
		%b : 논리(boolean) 형식으로 출력
		*/
		System.out.print("\n");
		int a = 10;	int b = 20;
		System.out.printf("a는 %d\n", a);
		System.out.printf("b는 %d\n", b);
		System.out.printf("a+b는 %d, a-b는 %d, a*b는 %d\n", a+b, a-b, a*b);
		
	}

}
