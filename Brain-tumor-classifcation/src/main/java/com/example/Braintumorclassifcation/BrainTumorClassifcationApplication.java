package com.example.Braintumorclassifcation;

import com.netflix.discovery.EurekaClient;
import com.netflix.discovery.shared.Application;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
@EnableAutoConfiguration
public class BrainTumorClassifcationApplication {

	@Autowired
	@Lazy
	private EurekaClient eurekaClient;

	@GetMapping("/")
	public String classification(){
		return "This brain tumor classification";
	}
	@GetMapping("/hello")
	public String hello(){
		String hello="";
		for(Application a : eurekaClient.getApplications().getRegisteredApplications()){
			hello +=a.getName()+" \n"+ a.	getInstances()+" ; \n";
		}
		return hello;
	}

	public static void main(String[] args) {
		SpringApplication.run(BrainTumorClassifcationApplication.class, args);
	}

}
