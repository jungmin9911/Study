package hello_java;
/*
스캐너(Scanner) - java.util이라는 패키지에 포함된 클래스
import 구문을 추가해 패키지 불러오기
*/
import java.util.Scanner;

public class java03 {

	public static void main(String[] args) {
		//스캐너를 이용하기 위해서는 스캐너 객체를 만들어야됨
		Scanner sc = new Scanner(System.in);
		//Scanner 클래스의 기능을 사용할 수 있는 sc라는 이름의 객체(모듈)를 만든다는 뜻
		
		System.out.print("이름을 입력하세요 : ");
		String name = sc.next();
		System.out.println("당신의 이름은 " + name + "이군요.");
		//sc가 스캔한 문자열을 name이라는 변수에 저장하고 println을 이용해 출력한 코드
		
		/*
		스캐너의 메소드 
		- nextInt()는 int 데이터 입력
		- nextFloat()은 float 데이터 입력 
		- nextLine()은 줄바꿈 전까지 쓴 문자열 읽기
		*/
		
		System.out.print("단어를 입력하세요 : ");
		String word = sc.next();
		
		System.out.print("정수를 입력하세요 : ");
		int num = sc.nextInt();
		
		System.out.print("실수를 입력하세요 : ");
		float f = sc.nextFloat();
		
		System.out.print("문장을 입력하세요 : ");
		sc.nextLine();
		String sentence = sc.nextLine();
		
		System.out.println("입력한 것들을 모두 모아볼까요?");
		System.out.printf("단어는 %s / 정수는 %d / 실수는 %f / 문장은 '%s'", word, num, f, sentence);
		
		sc.close();
		//스캐너를 닫지 않으면 warning이 뜸
	}

}
