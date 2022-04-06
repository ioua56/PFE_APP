package com.example.Brain_Tumor_Pathology;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@EnableEurekaServer
public class BrainTumorPathologyApplication {



	public static void main(String[] args) {
		SpringApplication.run(BrainTumorPathologyApplication.class, args);
	}

}
