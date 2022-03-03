package com.example.Braintumor;

import com.netflix.discovery.DiscoveryClient;
import com.netflix.discovery.EurekaClient;
import com.netflix.discovery.shared.Application;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.loadbalancer.LoadBalanced;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
@EnableAutoConfiguration
@EnableEurekaClient
public class BrainTumorApplication {

	@Autowired
	@Lazy
	private EurekaClient eurekaClient;



	@GetMapping("/hello")
	public String hello(){
		String hello="";
		for(Application a : eurekaClient.getApplications().getRegisteredApplications()){
			hello +=a.getName()+" \n"+ a.getInstances()+" ; \n";
		}
		return hello;
	}

	public static void main(String[] args) {
		SpringApplication.run(BrainTumorApplication.class, args);
	}

}
