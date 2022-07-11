package mit.edu.tv;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.mongo.MongoAutoConfiguration;

@EnableAutoConfiguration(exclude={MongoAutoConfiguration.class})
@SpringBootApplication
public class TvApplication {

	public static void main(String[] args) {
        System.out.println("--- Hello World! ---");
		SpringApplication.run(TvApplication.class, args);
	}

}
