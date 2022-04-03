package com.example.Brain_Tumor_Pathology;

import com.netflix.discovery.EurekaClient;
import com.netflix.discovery.shared.Application;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@EnableEurekaServer
@EnableEurekaClient
@RestController
public class BrainTumorPathologyApplication {

	@Autowired
	@Lazy
	private EurekaClient eurekaClient;

	// Get api that returns all services



	@GetMapping("/hello")
	public String hello(){
		String hello="Hello world";
		for(Application a : eurekaClient.getApplications().getRegisteredApplications()){
			hello +=a.getName()+" \n"+ a.getInstances()+" ; \n";
		}
		return hello;
	}


	public static void main(String[] args) {
		SpringApplication.run(BrainTumorPathologyApplication.class, args);
	}

}
