package vn.ptit.duongvct.nlp.week1;


import vn.pipeline.VnCoreNLP;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class Week1Application {

	public static void main(String[] args) throws IOException {
		String[] annotators = {"pos", "ner", "parse"};
		VnCoreNLP pipeline = new VnCoreNLP(annotators);
		String str = """
				Hôm nay tôi     đi     học lúc    7 giờ sáng tại cơ sở mới ở  Số 33 Đại Mỗ, Phường     Xuân Phương,    Thành phố Hà Nội.
				""";
		String cleanedText = cleanText(str);
		System.out.println(cleanedText);

	}
	private static String cleanText(String s) {
		List<String> list = Arrays.stream(s.split(" ")).toList();
		StringBuilder res = new StringBuilder();
		list.forEach(ss -> res.append(ss).append(" "));
		return res.toString().trim();
	}

}
